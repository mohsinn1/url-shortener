import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
# Fallback to localhost if MONGO_URI is missing (to prevent hard crashes locally)
if not MONGO_URI:
    client = MongoClient()
else:
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) 

db = client.shortener_db
collection = db.urls
from pydantic import BaseModel
from datetime import datetime, timezone
import random, string
from pymongo import ReturnDocument
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any frontend to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLCreate(BaseModel):
    url: str



@app.post("/shorten", status_code=201)
def create_short_url(payload: URLCreate, request: Request):
    
    original_url = payload.url
    if not original_url.startswith(("http://", "https://")):
        original_url = "https://" + original_url

    options = string.ascii_letters + string.digits
    code = ''.join(random.choices(options, k=6))
    base = str(request.base_url)
    link = base + code
    collection.insert_one(
        {
            'url' : original_url,
            'code' : code
        }
    )
    return link



@app.get('/{short_code}')
def redirect_url(short_code : str):
    target_url = collection.find_one({'code': short_code})
    if not target_url:
        raise HTTPException(404, detail="URL not found")
    else:
        return RedirectResponse(target_url['url'])
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


