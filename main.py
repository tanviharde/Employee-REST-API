
from typing import List, Literal, Optional

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(title="Employee API", version="1.0.0")
@app.get("/")
def root():
    return {
        "message": "Welcome to the Employee REST API",
        "docs": "/docs",
        "endpoints": [
            "GET /employees",
            "GET /employees/{employee_id}",
            "POST /employees",
            "PATCH /employees/{employee_id}/status"
        ]
    }

EmployeeStatus = Literal["Active", "Inactive"]


class Employee(BaseModel):
    id: int
    name: str
    department: str
    status: EmployeeStatus


class EmployeeCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=1)
    department: str = Field(..., min_length=1)


class StatusUpdate(BaseModel):
    status: EmployeeStatus


employees: List[Employee] = [
    Employee(id=1, name="Rahul Sharma", department="Engineering", status="Active"),
    Employee(id=2, name="Priya Patel", department="HR", status="Active"),
    Employee(id=3, name="Amit Verma", department="Engineering", status="Inactive"),
]


def find_employee(employee_id: int) -> Optional[Employee]:
    for employee in employees:
        if employee.id == employee_id:
            return employee
    return None


def generate_id() -> int:
    return max((employee.id for employee in employees), default=0) + 1


@app.get("/employees", response_model=List[Employee])
def get_employees(department: Optional[str] = Query(default=None)):
    if department is None:
        return employees

    department = department.strip().lower()

    return [
        employee for employee in employees
        if employee.department.lower() == department
    ]


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    employee = find_employee(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with id {employee_id} not found"
        )

    return employee


@app.post(
    "/employees",
    response_model=Employee,
    status_code=status.HTTP_201_CREATED
)
def create_employee(payload: EmployeeCreate):
    new_employee = Employee(
        id=generate_id(),
        name=payload.name,
        department=payload.department,
        status="Active"
    )

    employees.append(new_employee)
    return new_employee


@app.patch("/employees/{employee_id}/status", response_model=Employee)
def update_employee_status(employee_id: int, payload: StatusUpdate):
    employee = find_employee(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with id {employee_id} not found"
        )

    employee.status = payload.status
    return employee
