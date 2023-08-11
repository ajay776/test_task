# Worker, Unit, and Visit API Documentation

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
