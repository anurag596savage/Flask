from unittest import result
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help='This field can not be empty!'
    )
    @classmethod
    def Find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="SELECT * FROM Items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"Item":{"name":row[0],"price":row[1]}}
        return None

    @jwt_required()
    def get(self,name):
        item = self.Find_by_name(name)
        if item:
            return item,200
        return {"Message":"Item with the name '{}' could not be found!".format(name)},404

    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO Items VALUES(?,?)"
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()

    def post(self,name):
        item = self.Find_by_name(name)
        if item:
            return {"Message":"Item with the name '{}' already exits!".format(name)},400

        data = Item.parser.parse_args()
        item = {
            'name':name,
            'price':data['price']
        }
        try:
            self.insert(item)
        except:
            return {"Message":"An error occured inserting the item!"},500

        return item,201
    
    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="DELETE FROM Items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {"Message":"Item deleted!"}
    
    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="UPDATE Items SET price=? WHERE name=?"
        cursor.execute(query,(item['price'],item['name']))
        connection.commit()
        connection.close()
    
    def put(self,name):
        data = Item.parser.parse_args()
        updated_item = {
            'name':name,
            'price':data['price']
        }
        item = self.Find_by_name(name)
        if item:
            try:
                self.update(updated_item)
            except:
                return {"Message":"An error occured during updation of the item!"},500
        else:
            try:
                self.insert(updated_item)
            except:
                return {"Message":"An error occured during insertion of the item!"},500
            

        return updated_item

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM Items"
        result = cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        connection.close()
        return {"Items":items},200
    