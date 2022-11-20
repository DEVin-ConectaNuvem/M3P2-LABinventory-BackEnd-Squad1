from datetime import datetime
from bson import ObjectId, json_util
from src.app import mongo_client
from src.app.utils import convert_id

import re


class Database(object):
    def __init__(self, collection):
        self.collection = collection

    @staticmethod
    def format_return( response):
        list_response = []
        
        if isinstance(response, list):
            for item in response:
                item = convert_id(item)
                list_response.append(item)
            return list_response
        else:
            response = convert_id(response)
            return response

    def create(self, data):
        try:
            data["createdAt"] = datetime.utcnow()
            data["updatedAt"] = datetime.utcnow()
            response = mongo_client[self.collection].insert_one(data)
            result = {"id": str(response.inserted_id)}

            return result
        except Exception as e:
            return {"error": str(e)}

    def get_data_with_paginate(self, data):
        try:
            response = list(
                mongo_client[self.collection]
                .find(data["filter"])
                .skip(data["skip"])
                .limit(data["limit"])
            )
            response = self.format_return(response)
            
            result = {
                "rows": response,
                "totalRows": self.count(data["filter"])
            }

            return result
        except Exception as e:
            return {"error": str(e)}

    def get_one(self, data):
        try:
            data_with_like = [
                {key: {"$regex": re.compile(value, re.IGNORECASE)}}
                for key, value in data.items()
            ]
            for item in data_with_like:
                data.update(item)

            response = mongo_client[self.collection].find_one(data)
            response = self.format_return(response)

            return response
        except Exception as e:
            return {"error": str(e)}

    def get_all(self):
        try:
            response = list(mongo_client[self.collection].find())
            response = self.format_return(response)
            result = {
                "data": response,
                "totalRows": self.count({})
            }

            return result
        except Exception as e:
            return {"error": str(e)}

    def get_by_id(self, id):
        try:
            response = mongo_client[self.collection].find_one(
                {"_id": ObjectId(id)}
            )
            response = self.format_return(response)

            return response
        except Exception as e:
            return {"error": str(e)}

    def update(self, data):
        try:
            id = {"_id": ObjectId(data["id"])}
            data["dataset"]["updatedAt"] = datetime.utcnow()
            
            data_set = {"$set": data["dataset"]}
            response = mongo_client[self.collection].update_one(id, data_set)
            if response.matched_count > 0:
                return {
                    "message": "Data updated successfully",
                    "status": 200,
                }
        except Exception as e:
            return {"error": str(e)}

    def delete(self, data):
        try:
            response = mongo_client[self.collection].delete_one(data)
            response = self.format_return(response)

            return response
        except Exception as e:
            return {"error": str(e)}

    def count(self, data):
        try:
            response = mongo_client[self.collection].count_documents(data)
            return response
        except Exception as e:
            return {"error": str(e)}
