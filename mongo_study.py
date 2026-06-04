import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.faw86h6.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

databases = client.list_databases()
print(databases)
for db in databases:
    print(db)

db_shop = client.shop

collection_books = db_shop.books
collection_phones = db_shop['phones']

# CREATE
# add one document
book = {'title': '10 negro', "price": 365, 'description': "English classic detective"}
collection_books.insert_one(book)





















