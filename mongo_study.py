import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import ObjectId

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
# created_phone = collection_phones.insert_one(phone)
# print(created_phone)

# add many
phones = [
    {'title': 'iPhone 17', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 16', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 15', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 14', "price": 65000, 'description': "cool", 'is_restored': True},
]
# created_phones = collection_phones.insert_many(phones)
# print(created_phones)


# READ
# first
first_phone = collection_phones.find_one()
print(first_phone)

query = {
    # '_id': ObjectId('6a21a9d65f7f195a50597ade'),
    'price': 65000
}
wanted_book = collection_phones.find_one(query)
print(wanted_book)

# find_many



# all_phones = collection_phones.find()

query = {'title': 'iPhone 17'}
query = {'price': 65111}
query = {'price': {"$gt": 65000}}
query = {'price': {"$gte": 65000}}
query = {'price': {"$gt": 65000, "$lt": 68000}}
query = {'price': {"$gt": 65000, "$lte": 68000}, 'title': 'iPhone 15'}






all_phones = collection_phones.find(query)
# print(list(all_phones))
print(all_phones)

for phone in all_phones:
    print(phone)
























