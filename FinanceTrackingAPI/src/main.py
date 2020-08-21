from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.test import Test, TestSchema

app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route('/tests')
def get_tests():
    # fetching from the database
    session = Session()
    test_records = session.query(Test).all()

    # transforming into JSON-serializable objects
    schema = TestSchema(many=True)
    tests = schema.dump(test_records).data

    # serializing as JSON
    session.close()
    return jsonify(tests)

@app.route('/tests', methods=['POST'])
def add_test():
    # mount test object
    posted_test = TestSchema(only=('title', 'description'))\
        .load(request.get_json())

    test = Test(**posted_test.data, created_by="HTTP post request")

    # persist test
    session = Session()
    session.add(test)
    session.commit()

    # return created test record
    new_test = TestSchema().dump(test).data
    session.close()
    return jsonify(new_test), 201

    