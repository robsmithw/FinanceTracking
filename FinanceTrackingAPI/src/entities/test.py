from sqlalchemy import Column, String
from marshmallow import Schema, fields
from .entity import Entity, Base

class Test(Entity, Base):
    __tablename__ = 'test'

    title = Column(String(50))
    description = Column(String(100))

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

class TestSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
        