from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb+srv://admin:admin@cluster0.9p5wrdm.mongodb.net/?retryWrites=true&w=majority") #mongodb://localhost:27017
db = client["ecommerce"]

def get_collection(collection_name: str) -> Collection:
  return db[collection_name]