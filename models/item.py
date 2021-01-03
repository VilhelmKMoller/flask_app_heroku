import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    # SQ alchemy will search for only these values.
    id = db.Column(db.Integer, primary_key=True) # primary_key means that this value(id) is unique
    name = db.Column(db.String(80)) # (80) means max 80 char
    price = db.Column(db.Float(precision=2))

    # this is a foreign key meaning that it comes from another table(a table in the stores category)
    # it links the items and store files in the model package:
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # class method to find by name. Used by def get and def post
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELCT * FROM items WHERE name=name LIMIT 1

        # you can also filter by multiple things by using several .filter_by:
        #return ItemModel.query.filter_by(name=name).filter_by(id=1)

    def save_to_db(self): # was called update before
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
