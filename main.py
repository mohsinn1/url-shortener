from fastapi import FastAPI, HTTPException
from database import collection
from pydantic import BaseModel
from datetime import datetime, timezone
import random, string
from pymongo import ReturnDocument

app = FastAPI()

class URLCreate(BaseModel):
    url: str


@app.post("/shorten", status_code=201)
def create_short_url(request: URLCreate):
    pass
    # 1. Generate the short code using your helper function. DONE
    short = generate_code()

    # 2. Build the dataument: Create a Python dictionary. DONE

    data = {
        'url' : request.url,
        'shortCode' : short,
        'createdAt': datetime.now(timezone.utc),
        'updatedAt': datetime.now(timezone.utc),
        'accessCount': 0

    }



    # 3. Save to MongoDB: collection.insert_one(your_dictionary) DONE

    collection.insert_one(data)
    
    # 4. Cleanup & Return: MongoDB adds a weird object ID called '_id'. 
    #    Convert it to a string, rename it to 'id' (per the requirements),  DONE
    data['id'] = str(data['_id'])

    #    remove the original '_id', and return the dictionary! DONE

    del data['_id']
    return data



def generate_code():
    code = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return code



@app.get("/shorten/{shortCode}")
def get_url(shortCode:str):
    search = collection.find_one({'shortCode': shortCode})
    if not search:
        raise HTTPException(status_code=404, detail="URL Not Found")
    collection.update_one({'shortCode': shortCode},{"$inc": {'accessCount': 1}})
    search['accessCount'] += 1
    search['id'] = str(search['_id'])
    del search['_id']
    return search


@app.put("/shorten/{shortCode}")
def update_url(shortCode: str, request: URLCreate):
    search = collection.find_one({'shortCode':shortCode})
    if not search:
        raise HTTPException(status_code=404, detail="URL Not Found")
    collection.update_one({'shortCode':shortCode}, {'$set': {'url': request.url, 'updatedAt': datetime.now(timezone.utc)}})
    search['url'], search['updatedAt'] = request.url, datetime.now(timezone.utc)
    search['id'] = str(search['_id'])
    del search['_id']
    return search


@app.delete("/shorten/{shortCode}", status_code=204)
def delete_url(shortCode:str):
    result = collection.delete_one({'shortCode': shortCode})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="URL Not Found")


@app.get("/shorten/{shortCode}/stats")
def get_stats(shortCode:str):
    search = collection.find_one({'shortCode': shortCode})
    if not search:
        raise HTTPException(status_code=404, detail="URL Not Found")
    search['id'] = str(search['_id'])
    del search['_id']
    return search








