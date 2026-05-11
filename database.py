from pymongo import MongoClient
import certifi  
import os
from dotenv import load_dotenv

load_dotenv()



MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) 
db = client.shortener_db
collection = db.urls
