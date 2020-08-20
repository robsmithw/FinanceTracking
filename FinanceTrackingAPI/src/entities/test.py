from sqlalchemy import Column, String

from .entity import Entity, Base


class Test(Entity, Base):
    __tablename__ = 'test'

    title = Column(String(50))
    description = Column(String(100))

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        