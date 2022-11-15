from .database import Database

class inventoryService:
    def __init__(self):
        self.db = Database('items')
        
    def create_inventory(self, inventory):
        try:
            return self.db.create(inventory)
        except Exception as e:
            # error_details = json.loads(e.error).errInfo
            return e

    def get_inventory(self):
        try:
            return self.db.get_all()
        except Exception as e:
            return e
        
    def find_inventory(self, data):
        try:
            return self.db.get_one(data)
        except Exception as e:
            return e
    
    def get_inventory_by_id(self, inventory_id):
        try:
            return self.db.get_by_id(inventory_id)
        except Exception as e:
            return e
        
    def update_inventory(self, data):
        try:
            return self.db.update(data)
        except Exception as e:
            return e
            
    def delete_inventory(self, inventory_id):
        try:
            return self.db.delete(inventory_id)
        except Exception as e:
            return e
