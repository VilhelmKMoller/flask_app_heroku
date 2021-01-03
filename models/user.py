import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    # SQ alchemy will search for only these values.
    id = db.Column(db.Integer, primary_key=True) # primary_key means that this value(id) is unique
    username = db.Column(db.String(80)) # (80) means max 80 char
    password = db.Column(db.String(80))

    #store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    #store = db.relationship('StoreModel')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # SELCT * FROM users WHERE username = username LIMIT 1

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # SELCT * FROM users WHERE id = _id LIMIT 1
