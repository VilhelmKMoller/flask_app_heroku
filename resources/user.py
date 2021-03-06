import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    # this means that the parser will expect a username
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    # this means that the parser will expect a password
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self):
        # test if the data fits the format using parser
        data = UserRegister.parser.parse_args()

        # this tests if the username allready exists:
        if UserModel.find_by_username(data['username']):
            return {'message': "A user with username '{}' already exists.".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
