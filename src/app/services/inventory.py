import json
from bson import json_util
from .database import Database
from src.app.validators import (
    decorator_validate_types,
    decorator_validate_required_keys,
)
from src.app import mongo_client

class inventoryService:
    def __init__(self):
        self.db = Database('items')
        self.collection = "items"
    
    @decorator_validate_types
    @decorator_validate_required_keys
    def create_inventory(self, *args):
        try:
            data = args[0]
            return self.db.create(data)
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
    
    @decorator_validate_types
    @decorator_validate_required_keys
    def update_inventory(self, *args):
        try:
            data = args[0]
            return self.db.update(data)
        except Exception as e:
            return e
            
    def delete_inventory(self, inventory_id):
        try:
            return self.db.delete(inventory_id)
        except Exception as e:
            return e

    def get_analytics(self):
        try:
            total_value_items = mongo_client[self.collection].aggregate([
                            {
                                '$group': {
                                    '_id': None, 
                                    'totalValue': {
                                        '$sum': '$value'
                                    }
                                }
                            }
                        ])
            total_items = mongo_client[self.collection].count_documents({})
            total_borrowed = mongo_client[self.collection].aggregate([
                            {
                                '$match': {
                                    'collaborator': {
                                        '$ne': None
                                    }
                                }
                            }, {
                                '$count': 'borrowed'
                            }
                        ])
            total_collabs = mongo_client["employers"].count_documents({})

            json_total_value_items = json_util.dumps(total_value_items)
            json_total_items = json_util.dumps(total_items)
            json_total_borrowed = json_util.dumps(total_borrowed)
            json_total_collabs = json_util.dumps(total_collabs)

            response = {
                "total_value": json.loads(json_total_value_items)[0]["totalValue"],
                "total_items": json.loads(json_total_items),
                "total_borrowed": json.loads(json_total_borrowed)[0]["borrowed"],
                "total_collabs": json.loads(json_total_collabs)
            }
            return response
        except Exception as e:
            return {"error": e}