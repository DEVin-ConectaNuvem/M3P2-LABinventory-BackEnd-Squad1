from src.app.validators import (
    decorator_validate_types,
    decorator_validate_required_keys,
)
from .database import Database


class Employees_Service:
    def __init__(self):
        self.db = Database("employees")

    @decorator_validate_types
    @decorator_validate_required_keys
    def create_employee(self, *args):
        try:
            object = args[0]
            email = object["email"]
            validate_email = self.db.get_one({"email": email})
            if validate_email:
                return {"error": "Email already exists", "status": 400}

            return self.db.create(object)
        except Exception as e:
            return e

    def get_employees(self, payload=None):
        try:
            if payload:
                return self.db.get_data_with_paginate(payload)
            else:
                res = self.db.get_all()
                return res
        except Exception as e:
            return e

    def get_employee(self, data):
        try:
            return self.db.get_one(data)
        except Exception as e:
            return e

    def get_employee_by_id(self, employee_id):
        try:
            return self.db.get_by_id(employee_id)
        except Exception as e:
            return e

    @decorator_validate_types
    @decorator_validate_required_keys
    def update_employee(self, *args):
        try:
            data = args[0]
            return self.db.update(data)
        except Exception as e:
            return e

    def delete_employee(self, *args):
        try:
            data = args[0]
            return self.db.delete(data)
        except Exception as e:
            return e
