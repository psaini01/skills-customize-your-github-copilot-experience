# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

@app.get("/items")
def get_items():
    return items

@app.post("/items", status_code=201)
def create_item(item: Item):
    items.append(item)
    return item
