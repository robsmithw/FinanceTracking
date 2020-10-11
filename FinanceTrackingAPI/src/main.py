from flask import Flask, jsonify, request, send_file, safe_join
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.test import Test, TestSchema

app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/downloadTemplate')
def get_template():
    try:
        filepath = f'D:\\Temp\\template.csv'
        return send_file(filepath, as_attachment=True)
    except FileNotFoundError:
        return 404

@app.route('/tests')
def get_tests():
    # fetching from the database
    session = Session()
    test_records = session.query(Test).all()

    # transforming into JSON-serializable objects
    schema = TestSchema(many=True)
    tests = schema.dump(test_records)

    # serializing as JSON
    session.close()
    return jsonify(tests)

@app.route('/tests', methods=['POST'])
def add_test():
    # mount test object
    posted_test = TestSchema(only=('title', 'description'))\
        .load(request.get_json())

    test = Test(**posted_test, created_by="HTTP post request")

    # persist test
    session = Session()
    session.add(test)
    session.commit()

    # return created test record
    new_test = TestSchema().dump(test)
    session.close()
    return jsonify(new_test), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0')
