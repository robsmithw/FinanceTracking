from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema, fields
from .entity import Entity, Base

class TransactionTypeMap(Entity, Base):
    __tablename__ = 'transaction_type_map'

    keyword = Column(String(50))
    type_id = Column(Integer)
    active = Column(Boolean)

    def __init__(self, keyword, type_id, active, created_by):
        Entity.__init__(self, created_by)
        self.keyword = keyword
        self.type_id = type_id
        self.active = active

class TransactionTypeMapSchema(Schema):
    id = fields.Integer()
    keyword = fields.Str()
    type_id = fields.Integer()
    active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
