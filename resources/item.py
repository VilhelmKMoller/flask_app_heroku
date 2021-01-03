from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Item(Resource):
    # this request parsin can be used to check the input data is as we want it before we include it:
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
    )

    # if you place the jwt_required in front then this part will require a token to be executed.
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # test if the data fits the format
        data = Item.parser.parse_args()

        item = ItemModel(name, **data) # **data = data['price'], data['store_id']
        # runs def that insert the item item
        try:
            item.save_to_db()
        except:
            return {"message" : "An error occurred insert the item"}, 500 # 500 == internal server error

        return item.json(), 201 # 201 is status code for created

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message' : 'Item deleted'}

    def put(self, name):
        # test if the data fits the format
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        # using list comprehention:
        return {"items" : [item.json() for item in ItemModel.query.all()]} # SELECT * FROM items

        # alternative to above code:
        # using lambda function:
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
