# Worker, Unit, and Visit API Documentation

Before you begin, make sure to follow these steps:

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv

2. Install requirements.txt
    ```bash
    pip install -r requirements.txt

## List Units Linked to Specified Worker

**Endpoint:** `/api/get_units/`

**Method:** GET

**Parameters:**
- `phone` (string, required): Phone number of the worker.

**Response:**
```json
[
    {
        "id": 1,
        "name": "Unit 1"
    },
    {
        "id": 2,
        "name": "Unit 2"
    }
]

## Make a Visit

**Endpoint:** `/api/make_visit/`

**Method:** POST

**Request Body:**
```json
    {
        "unit_pk": 1,
        "latitude": 37.7749,
        "longitude": -122.4194
    }


**Response:**
```json
{
    "id": 1,
    "datetime": "2023-08-11T12:34:56Z"
}