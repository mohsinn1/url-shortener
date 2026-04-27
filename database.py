from pymongo import MongoClient
import certifi  
import os

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) 
db = client.shortener_db
collection = db.urls
