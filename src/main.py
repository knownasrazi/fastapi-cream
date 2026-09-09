from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="fastapi-cream", version="1.0.0")

class Item(BaseModel):
    id: int
    name: str
    price: float

# In-memory store - a person would keep it simple first
items: List[Item] = []
next_id = 1

@app.get("/")
async def root():
    return {"name": "fastapi-cream", "tag": "FastAPI, in clean."}

@app.get("/health")
async def health():
    return {"status": "ok", "items": len(items)}

@app.get("/items", response_model=List[Item])
async def list_items():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    global next_id
    # Hand-crafted: auto-increment, not trusting client id
    new_item = Item(id=next_id, name=item.name, price=item.price)
    next_id += 1
    items.append(new_item)
    return new_item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global items
    before = len(items)
    items = [it for it in items if it.id != item_id]
    if len(items) == before:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": item_id}
