from src.app.validators import (
    decorator_validate_types,
    decorator_validate_required_keys,
)
from .database import Database


class EmployersService:
    def __init__(self):
        self.db = Database("employers")

    @decorator_validate_types
    @decorator_validate_required_keys
    def create_employer(self, *args):
        try:
            object = args[0]
            return self.db.create(object)
        except Exception as e:
            # error_details = json.loads(e.error).errInfo
            return e

    def get_employers(self):
        try:
            return self.db.get_all()
        except Exception as e:
            return e

    def get_employer(self, data):
        try:
            return self.db.get_one(data)
        except Exception as e:
            return e

    def get_employer_by_id(self, employer_id):
        try:
            return self.db.get_by_id(employer_id)
        except Exception as e:
            return e

    @decorator_validate_types
    @decorator_validate_required_keys
    def update_employer(self, *args):
        try:
            data = args[0]
            return self.db.update(data)
        except Exception as e:
            return e

    @decorator_validate_types
    @decorator_validate_required_keys
    def delete_employer(self, *args):
        try:
            data = args[0]
            return self.db.delete(data)
        except Exception as e:
            return e
