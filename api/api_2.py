# Import FastAPI and Pydantic's BaseModel
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create an instance of the FastAPI class
app = FastAPI()

# A simple database simulation using a dictionary
fake_database = {}

# Pydantic model for item
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# GET route to read the root
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI example application!"}

# GET route to get an item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in fake_database:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_database[item_id]

# POST route to create an item
@app.post("/items/")
async def create_item(item: Item):
    item_id = len(fake_database) + 1
    fake_database[item_id] = item
    return item

# GET route with both path parameters and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, query: Optional[str] = None):
    return {"user_id": user_id, "item_id": item_id, "query": query}
