from src.app.validators import adjust_errors_from_mongoschema
from src.app.services import inventory as inventory_service
from flask import Blueprint, request, json
from flask.wrappers import Response
from bson import json_util

inventory = Blueprint("inventory", __name__, url_prefix="/inventory")
inventoryService = inventory_service.inventoryService()


@inventory.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = inventoryService.create_inventory(data, "items")
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(json_util.dumps(response), status=201, mimetype="application/json")


@inventory.route("/", methods=["GET"])
def get_all():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    searchField = request.args.get("searchField", None, type=str)
    searchValue = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operator", None, type=str)
    payload = {}
    if page and limit:
        payload = {
            "filter": {searchField: searchValue} if searchField else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventoryService.get_inventory(payload)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/<id>", methods=["GET"])
def get_by_id(id):
    response = inventoryService.get_inventory_by_id(id)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )

@inventory.route("/list", methods=["GET"])
def list():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    searchField = request.args.get("searchField", None, type=str)
    searchValue = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operator", None, type=str)
    payload = {}
    if page and limit:
        payload = {
            "filter": {searchField: searchValue} if searchField else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventoryService.get_inventory_list(payload)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = inventoryService.update_inventory(data, "items")
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/delete", methods=["DELETE"])
def delete():
    response = inventoryService.delete_inventory(request.args)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/analytics", methods=["GET"])
def get_analytics():
    response = inventoryService.get_analytics()
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json.dumps(response), status=200, mimetype="application/json"
    )
