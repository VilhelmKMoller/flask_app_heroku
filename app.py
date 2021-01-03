from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# import security python script:
from security import authenticate, identity
# import user register from from resource package. enables creating users in the system
from resources.user import UserRegister
# import Items classes from resource package:
from resources.item import Item, ItemList
# import the db file
from db import db
# improt store from resurces
from resources.store import Store, StoreList

app = Flask(__name__)

# name of data base and data file that we use:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICIATIONS'] = False
# this is the secret code to decrypt your passwords:
app.secret_key = "vilhelm"
api = Api(app)

# creats the data.db file, if it has not be created allready
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity) #/auth (authenticate user)

# the text '' means that it will call the api if the http ends with ex /items. (called the endpoint):
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# means that you can only run the app if you are running the app.py script
# so if you are loading the app.py script into another .py file then it will not run
# __name__ == 'main'. means that this .py file is the main file.
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
