from bson import json_util
from flask import Blueprint, json, request
from flask.wrappers import Response

from src.app.middlewares.auth import requires_access_level
from src.app.services.inventory import Inventory_Service
from src.app.validators import adjust_errors_from_mongoschema

inventory = Blueprint("inventory", __name__, url_prefix="/inventory")
inventorys_service = Inventory_Service()
"""
/create - POST
    request:
        body = {
            codPatrimonio : string - required : true
            title : string - required : true
            description : string - required : true
            category : string - required : true
            value : number - required : true
            brand : string - required : true
            model : string - required : true

    }
     
    responses:
        status 201:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/create", methods=["POST"])
@requires_access_level(["READ", "WRITE"])
def create():
    data = request.get_json()
    response = inventorys_service.create_inventory(data, "items")

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(json_util.dumps(response), status=201, mimetype="application/json")


"""
/list - GET
    request:
        possible params:
            searchField - (i.e. code - title - description)
            searchValue - (i.e. value that will be searched across the selected field)
            operatorSearch - (i.e. like)

        Example of search using params: /?searchField=code&searchValue=12&operatorSearch=like
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/", methods=["GET"])
@requires_access_level(["READ"])
def get_all():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    search_field = request.args.get("searchField", None, type=str)
    search_value = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operatorSearch", None, type=str)

    payload = {}
    if page and limit:
        payload = {
            "filter": {search_field: search_value} if search_field else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventorys_service.get_inventory(payload)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


"""
/<id> - GET
    request:
        use id as a param

    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/<id>", methods=["GET"])
@requires_access_level(["READ"])
def get_by_id(id):
    response = inventorys_service.get_inventory_by_id(id)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


"""
/list - GET
    request:
        possible params:
            searchField - (i.e. code - title - description)
            searchValue - (i.e. value that will be searched across the selected field)
            operatorSearch - (i.e. like)

        Example of search using params: /?searchField=code&searchValue=12&operatorSearch=like
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/list", methods=["GET"])
@requires_access_level(["READ"])
def list():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    search_field = request.args.get("searchField", None, type=str)
    search_value = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operatorSearch", None, type=str)

    payload = {}
    if page and limit:
        payload = {
            "filter": {search_field: search_value} if search_field else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventorys_service.get_inventory_list(payload)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


"""
/update - PATCH
    request:
        body = {
            id : id of the employee that will be updated
            dataset : {
                keys_to_be_changed : new_values
            }
        }
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/update", methods=["PATCH"])
@requires_access_level(["READ", "WRITE", "UPDATE"])
def update():
    data = request.get_json()
    response = inventorys_service.update_inventory(data, "items")

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


"""
/delete - DELETE
    request:
        body = {
            id : id of the item that will be deleted
        }
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/delete", methods=["DELETE"])
@requires_access_level(["READ", "WRITE", "UPDATE", "DELETE"])
def delete():
    response = inventorys_service.delete_inventory(request.args)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


"""
/analytics - GET
    request:
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@inventory.route("/analytics", methods=["GET"])
@requires_access_level(["READ"])
def get_analytics():
    response = inventorys_service.get_analytics()

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json.dumps(response), status=200, mimetype="application/json"
    )
