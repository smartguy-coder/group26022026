import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.faw86h6.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

# databases = client.list_databases()
# print(databases)
# for db in databases:
#     print(db)

# db_shop = client.shop
db_shop = client['outlet']

collection_books = db_shop.books
collection_phones = db_shop['phones']

# CREATE
# add one document
book = {'title': '10 negro', "price": 365, 'description': "English classic detective"}
collection_books.insert_one(book)

phone = {'title': 'iPhone 17', "price": 65000, 'description': "cool"}
created_phone = collection_phones.insert_one(phone)
print(created_phone)

# add many
phones = [
    {'title': 'iPhone 17', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 16', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 15', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 14', "price": 65000, 'description': "cool", 'is_restored': True},
]
created_phones = collection_phones.insert_many(phones)
print(created_phones)





























