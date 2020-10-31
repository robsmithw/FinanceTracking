import os
import sys
import json
import pandas as pd
from datetime import datetime
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.transactions import Transactions, TransactionsSchema
from .entities.transaction_types import TransactionTypes, TransactionTypesSchema
from .entities.transaction_type_map import TransactionTypeMap, TransactionTypeMapSchema
from .models.transaction import Transaction, TransactionEncoder

app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/getTotalAmount', methods=['GET'])
def get_total_amount():
    try:
        total_amount = 0

        # fetching from the database
        session = Session()
        transactionRecords = session.query(Transactions).all()

        for record in transactionRecords:
            total_amount += record.amount

        session.close()

        return jsonify(str(total_amount))
    except Exception as ex:
        print(ex, file=sys.stderr)
        return jsonify(ex), 500

@app.route('/downloadTemplate', methods=['GET'])
def get_template():
    try:
        filepath = os.path.join(os.getcwd(), 'template.csv')
        return send_file(filepath, as_attachment=True)
    except FileNotFoundError:
        return 404

@app.route('/processCsv', methods=['POST'])
def post_csv_report():
    try:
        if 'file' not in request.files:
            return jsonify('File not found to upload'), 400

        data = request.files['file']
        transactions = []
        dateFormat = '%m/%d/%Y'
        df = pd.read_csv(data)
        amount = 0
        for index, row in df.iterrows():
            formattedDate = datetime.strptime(row['Date'].strip(), dateFormat) #strip used because leading 0's are replaced by spaces
            trans = Transaction(row['Description'], row['Amount'], formattedDate)
            #store_transaction(trans)
            transactions.append(trans)

        return json.dumps(transactions, indent=4, sort_keys=True, cls=TransactionEncoder), 200
    except Exception as ex:
        print(ex, file=sys.stderr)
        return jsonify(ex), 500

@app.route('/saveTransactions', methods=['POST'])
def post_transactions():
    try:
        transactions = request.json
        if transactions is None:
            return "", 400

        all_trans = []
        for tran in transactions:
            curr_tran = Transaction(tran['description'], tran['amount'], tran['date'])
            store_transaction(curr_tran)
            all_trans.append(curr_tran)

        return json.dumps(all_trans, indent=4, sort_keys=True, cls=TransactionEncoder), 201
    except Exception as ex:
        print(ex, file=sys.stderr)
        return jsonify(ex), 500

# @app.route('/tests')
# def get_tests():
#     # fetching from the database
#     session = Session()
#     test_records = session.query(Test).all()

#     # transforming into JSON-serializable objects
#     schema = TestSchema(many=True)
#     tests = schema.dump(test_records)

#     # serializing as JSON
#     session.close()
#     return jsonify(tests)

# @app.route('/tests', methods=['POST'])
# def add_test():
#     # mount test object
#     posted_test = TestSchema(only=('title', 'description'))\
#         .load(request.get_json())

#     test = Test(**posted_test, created_by="HTTP post request")

#     # persist test
#     session = Session()
#     session.add(test)
#     session.commit()

#     # return created test record
#     new_test = TestSchema().dump(test)
#     session.close()
#     return jsonify(new_test), 201

def store_transaction(transaction: Transaction):
    transactionEntry = Transactions(transaction.description, transaction.amount, transaction.date, 'Upload')

    session = Session()
    session.add(transactionEntry)
    session.commit()

    session.close()
    return


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
