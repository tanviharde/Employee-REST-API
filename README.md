# Employee REST API

A REST API built with Python and FastAPI to manage employee records in memory.

## Requirements
- Python 3
- FastAPI
- Uvicorn

## Setup

Activate the virtual environment with `source venv/bin/activate`.
Install dependencies using `python -m pip install -r requirements.txt`.

## Run

Run `python -m uvicorn main:app --reload`.
Open http://127.0.0.1:8000/docs to test the API.

## Endpoints
- GET /employees — Get all employees; optionally filter by department.
- GET /employees/{employee_id} — Get an employee by ID.
- POST /employees — Create an employee with default Active status.
- PATCH /employees/{employee_id}/status — Update employee status to Active or Inactive.

Employee data is stored in memory and resets when the server restarts.
