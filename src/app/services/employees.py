from src.app.validators import (
    decorator_validate_required_keys,
    decorator_validate_types,
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
                return {"error": "Email informado já possui cadastro", "status": 400}

            return self.db.create(object)
        except Exception as e:
            return {"error": str(e)}

    def get_employees(self, req_args=None):
        try:
            if req_args:
                return self.db.get_data_with_paginate(req_args)
            else:
                res = self.db.get_all()
                return res
        except Exception as e:
            return {"error": str(e)}

    def get_employee_by_id(self, employee_id):
        try:
            return self.db.get_by_id(employee_id)
        except Exception as e:
            return {"error": str(e)}

    @decorator_validate_types
    @decorator_validate_required_keys
    def update_employee(self, *args):
        try:
            data = args[0]
            if "email" in data["dataset"]:
                email_initial = self.db.get_by_id(data["id"])["email"]
                email = data["dataset"]["email"]
                if email_initial != email:
                    exists_cod = self.db.get_one({"email": email})
                    if exists_cod:
                        return {
                            "error": "Email informado já possui cadastro",
                            "status": 400,
                        }

            return self.db.update(data)
        except Exception as e:
            return {"error": str(e)}

    def delete_employee(self, employee_id):
        try:
            return self.db.delete(employee_id)
        except Exception as e:
            return {"error": str(e)}
