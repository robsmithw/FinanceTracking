from sqlalchemy import Column, String, Boolean, DateTime
from marshmallow import Schema, fields
from .entity import Entity, Base

class TransactionTypes(Entity, Base):
    __tablename__ = 'transaction_types'

    transaction_type = Column(String(50))
    active = Column(Boolean)

    def __init__(self, transaction_type, active, created_by):
        Entity.__init__(self, created_by)
        self.transaction_type = transaction_type
        self.active = active

class TransactionTypesSchema(Schema):
    id = fields.Integer()
    transaction_type = fields.Str()
    active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
