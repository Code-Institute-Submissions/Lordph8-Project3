import pymongo
import os

MONGODB_URI = "mongodb+srv://root:7H3_4r73575@myfirstcluster-qpzww.mongodb.net/myFirstMDB?retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)