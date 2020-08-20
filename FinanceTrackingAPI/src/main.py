from .entities.entity import Session, engine, Base
from .entities.test import Test

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
tests = session.query(Test).all()

if not tests:
    # create and persist test record
    test_record = Test("SQLAlchemy MySQL Test", "Testing access to docker MySQL SQLAlchemy.", "rsmith")
    session.add(test_record)
    session.commit()
    session.close()

    # reload data
    tests = session.query(Test).all()

# show test records
print('Test records:')
for rec in tests:
    print(f'({rec.id}) {rec.title} - {rec.description} - Created by {rec.last_updated_by}')
    