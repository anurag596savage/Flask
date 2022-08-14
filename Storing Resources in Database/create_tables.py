import sqlite3

create_table_Users = "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY,username VARCHAR(25),password VARCHAR(25))"
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute(create_table_Users)
print("Table with the name as 'Users' created successfully!")

create_table_Items = "CREATE TABLE IF NOT EXISTS Items(name VARCHAR(25),price REAL)"
cursor.execute(create_table_Items)
print("Table with the name as 'Items' created successfully!")


connection.commit()
connection.close()


