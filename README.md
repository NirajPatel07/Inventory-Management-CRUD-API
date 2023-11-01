# Inventory Management CRUD API

![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

This is an API for managing and maintaining an inventory, providing Create, Read, Update, and Delete (CRUD) operations for items. It's built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Features

- List all items in the inventory.
- Retrieve specific item details by ID.
- Add new items to the inventory.
- Update existing item details.
- Delete items from the inventory.

## API Endpoints

### List All Items

- **URL:** `/items/`
- **Method:** `GET`
- **Description:** Get a list of all items in the inventory.

### Get a Specific Item by ID

- **URL:** `/items/{item_id}`
- **Method:** `GET`
- **Description:** Get details of a specific item by its ID.
- **Parameters:**
  - `item_id` (int, path): The ID of the item to retrieve.

### Add a New Item

- **URL:** `/items/`
- **Method:** `POST`
- **Description:** Add a new item to the inventory.
- **Request Body:** An example request body for adding a new item:
  ```json
  {
    "item_name": "New Item",
    "quantity": 10,
    "item_description": "A description of the new item."
  }
  ```

### Update an Existing Item

- **URL:** `/items/{item_id}`
- **Method:** `PUT`
- **Description:** Update the details of an existing item.
- **Parameters:**
  - `item_id` (int, path): The ID of the item to update.
  - `Request Body` An example request body for updating an item:
    ```json
    {
      "item_name": "Updated Item Name",
      "quantity": 20,
      "item_description": "Updated description."
    }
    ```

### Delete an Item

- **URL:** `/items/{item_id}`
- **Method:** `DELETE`
- **Description:** Delete an item from the inventory.
- **Parameters:**
  - `item_id` (int, path): The ID of the item to delete.

