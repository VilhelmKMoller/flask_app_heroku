import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    # SQ alchemy will search for only these values.
    id = db.Column(db.Integer, primary_key=True) # primary_key means that this value(id) is unique
    name = db.Column(db.String(80)) # (80) means max 80 char

    # back reference, verify that the store id matches
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # class method to find by name. Used by def get and def post
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELCT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self): # was called update before
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
