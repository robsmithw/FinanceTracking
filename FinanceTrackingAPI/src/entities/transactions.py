from sqlalchemy import Column, String, Numeric, DateTime
from marshmallow import Schema, fields
from .entity import Entity, Base

class Transactions(Entity, Base):
    __tablename__ = 'transactions'

    description = Column(String(50))
    amount = Column(Numeric(10,2))
    date = Column(DateTime)

    def __init__(self, description, amount, date, created_by):
        Entity.__init__(self, created_by)
        self.description = description
        self.amount = amount
        self.date = date

class TransactionsSchema(Schema):
    id = fields.Integer()
    description = fields.Str()
    amount = fields.Float()
    date = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
