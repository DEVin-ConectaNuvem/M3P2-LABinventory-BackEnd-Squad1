import json
from .database import Database

class EmployersService:
    def __init__(self):
        self.db = Database('employers')
        
    def create_employer(self, employer):
        try:
            return self.db.create(employer)
        except Exception as e:
            # error_details = json.loads(e.error).errInfo
            return e

    def get_employers(self):
        try:
            return self.db.get_all_employers()
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
        
    def update_employer(self, data):
        try:
            return self.db.update(data)
        except Exception as e:
            return e
            
    def delete_employer(self, employer_id):
        try:
            return self.db.delete(employer_id)
        except Exception as e:
            return e
