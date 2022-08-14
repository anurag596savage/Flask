import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def Find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE username=?"

        result = cursor.execute(query,(username,))

        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


    @classmethod
    def Find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM Users WHERE id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field can not be blank!'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field can not be blank!'
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        user = User.Find_by_username(data['username'])
        if user:
            return {"Message":"A user with the username already exists!"},400

        insert_query = "INSERT INTO Users VALUES(NULL,?,?)"
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute(insert_query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"Message":"User created successfully!"},201
