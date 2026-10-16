# Employee REST API

A REST API built using Python and FastAPI to manage employee records. Employee data is stored in memory; no database is required.

## Requirements
- Python 3.10 or later
- pip

## Setup and Installation

1. Extract the ZIP file or clone the repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment.

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the API

Start the server:

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

- **GET** `/employees` — Retrieve all employees; optionally filter by department using `?department=Engineering`.
- **GET** `/employees/{employee_id}` — Retrieve an employee by ID.
- **POST** `/employees` — Create an employee with default status `Active`.
- **PATCH** `/employees/{employee_id}/status` — Update status to `Active` or `Inactive`.

## Postman Testing

Import `Employee_API.postman_collection.json` into Postman. Ensure the API server is running before sending requests.

