from pymongo import MongoClient

client = MongoClient("mongodb+srv://saurabh16:xeKO1NgvR7TVYcMO@demo.hn2wgk8.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name=  db["todo_collection"]
