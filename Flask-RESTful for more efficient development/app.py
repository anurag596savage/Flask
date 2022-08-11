from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity


app = Flask(__name__)
app.secret_key = "Anurag@2000"
api = Api(app)

jwt = JWT(app,authenticate,identity)
# This is used to create a new endpoint '/auth' for our app which will be used to authenticate the user and return a JWT if match found 
# in the database when the user provides a username and password and this token will be used by client to identify the user when he wants 
# to retrieve data using GET method.


# In the code we have used a in memeory database in the form of Python List. It will store the items inside them as a dictionary.
items = []

# In case of RESTful API we deal with resources hence we create a class which is inherited from Resource and add some methods to it. 
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'price',
            type=float,
            required = True,
            help = 'This field can not be empty!'
        )
        # The parser defined above does not belong to an instance of the class but the class itself,so we do not have to use self keyword.

    # It implies that GET method will require web token in order for the user to retrieve information.If we do not provide the 
    # JWT or payload before making the GET request we will get status code 401 implying unauthorised access for invalid credentials.
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x:x['name']==name,items),None)
        # The filter() takes filtering function and sequence as input and return an object which in our case is a single item hence 
        # we do not need to convert it into a list.
        # The next() applied on the filter function returns the first occurence but if it does not find anything it will return None.
        return {'item':item},200 if item else 404

        """
        for item in items:
            if item['name']==name:
                return item
                # In this we do not need to jsonify the data we want to return it is done by RESTful API automatically.
        
        return {'Item':None},404
        # Though Postman return null is item is not found but many frameworks like Angular JS does not accept anything other than JSON so # it is a good practice to return dictionary instead of null.Along with that we also pass the status code 404 for error which
        # otherwise returns code 200 which implies successful request.

        """

    def post(self,name):
        '''
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required = True,
            help = 'This field can not be empty!'
        )
        '''
        if next(filter(lambda x:x['name']==name,items),None):
            return {'Message':"An item with name '{}' already present".format(name)},400
            # In this we do not create an item if an item with the same name already exists.
            # If there already exists such a item we return status code 400 for bad request.
        '''
        data = request.get_json()
        
        # In the above line if we have not set the Content Type in the header section it will throw an error. Hence to avoid it we have 
        # to set a parameter inside get_json() - force=True(It ignores the header section and jumps to body) or silent=True(It returns # # None if the header section is not there).

        '''
        data =  Item.parser.parse_args()
        
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201
        # Along with the item created we also the associated HTTP status code 201 for creation of items in server side.
    

    def delete(self,name):
        global items
        # If we do not include the above line a local variable gets created inside the delete method and in the line below we 
        # define the variable using itself which is not correct.
        items = list(filter(lambda x:x['name']!=name,items))
        return {'Message':'Item Deleted'}
    
    def put(self,name):
        ''' 
        data = request.get_json()
        '''

        '''
        parser = reqparse.RequestParser()
        # We use a request parser object to process the payload
        parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'This field can not be left blank!'
        )

        '''
        data = Item.parser.parse_args()
        # From the above line the parser will erase all the data provided in payload except the 'price' field.
        item = next(filter(lambda x:x['name']==name,items),None)

        if item is None:
            item = {
                'name':name,
                'price':data['price']
            }
            items.append(item)
        else:
            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return {'items':items}


# The endpoint specified below would work for both GET and POST requests. We may send some additional payload in JSON as for POST method.
api.add_resource(Item,'/item/<string:name>')
# TRhe endpoint specified below would return the list of items(dictionaries).
api.add_resource(ItemList,'/items')


app.run(port=5001,debug=True)

