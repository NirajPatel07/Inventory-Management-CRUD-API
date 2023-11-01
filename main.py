from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

inventory = {}
item_id_counter = 1


class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    item_description: Optional[str] = None


# Route to list all items
@app.get("/items/", response_model=dict)
async def list_items():
    """
    Get a list of all items in the inventory.
    """
    return {"inventory": inventory}


# Route to get a specific item by ID
@app.get("/items/{item_id}", response_model=dict)
async def get_item(item_id: int):
    """
    Get details of a specific item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        dict: Item details.
    """
    if item_id in inventory:
        return {"item_id": item_id, "item_details": inventory[item_id]}
    raise HTTPException(status_code=404, detail="Item not found")


# Route to add a new item
@app.post("/items/", response_model=dict)
async def add_item(item: ItemUpdate):
    """
    Add a new item to the inventory.

    Args:
        item (ItemUpdate): Item details to add.

    Returns:
        dict: Confirmation message and the assigned item ID.
    """
    global item_id_counter
    inventory[item_id_counter] = item
    item_id_counter += 1
    return {"message": "Item added", "item_id": item_id_counter - 1}


# Route to update an existing item
@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item_details: ItemUpdate):
    """
    Update the details of an existing item.

    Args:
        item_id (int): The ID of the item to update.
        item_details (ItemUpdate): New item details.

    Returns:
        dict: Confirmation message and the updated item ID.
    """
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_details.item_name is not None:
        inventory[item_id].item_name = item_details.item_name

    if item_details.quantity is not None:
        inventory[item_id].quantity = item_details.quantity

    if item_details.item_description is not None:
        inventory[item_id].item_description = item_details.item_description

    return {"message": "Item Updated", "item_id": item_id}


# Route to delete an item
@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    """
    Delete an item from the inventory.

    Args:
        item_id (int): The ID of the item to delete.

    Returns:
        dict: Confirmation message and the deleted item ID.
    """
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")

    del inventory[item_id]
    return {"message": "Item Deleted", "item_id": item_id}
