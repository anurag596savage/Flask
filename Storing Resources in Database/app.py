from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT

from item import Item,ItemList

from user import UserRegister

from security import authenticate,identity

app = Flask(__name__)
app.secret_key="Anurag@2000"
api = Api(app)

jwt = JWT(app,authenticate,identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    app.run(port=6001,debug=True)

