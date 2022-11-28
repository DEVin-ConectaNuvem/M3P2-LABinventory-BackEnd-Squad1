from bson import json_util
from flask import Blueprint, request
from flask.wrappers import Response

from src.app.middlewares.auth import requires_access_level
from src.app.services import employees as employees_service
from src.app.validators import adjust_errors_from_mongoschema

employees = Blueprint("employees", __name__, url_prefix="/employees")
employee_service = employees_service.Employees_Service()

"""
/create - POST
    request:
        body = {
            name : string - required : true
            email : string - required : true
            phone : string - required : true
            position : string - required : true
            gender : string - required : true
            zipcode : string - required : true
            birthday : string - required : true
            city : string - required : true
            state : string - required : true
            city : string - required : true
            neighborhood : string - required : true
            houseNumber : number - required : true
            complement : string - required : true
            reference : string - required : true
    }
     
    responses:
        status 201:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@employees.route("/create", methods=["POST"])
@requires_access_level(["READ", "WRITE"])
def create():
    data = request.get_json()
    response = employee_service.create_employee(data, "employees")

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(json_util.dumps(response), status=201, mimetype="application/json")


"""
/ - GET
    request:
        possible params:
            searchField - (i.e. name - position - email)
            searchValue - (i.e. value that will be searched across the selected field)
            operatorSearch - (i.e. like)

        Example of search using params: /?searchField=name&searchValue=ana&operatorSearch=like
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@employees.route("/", methods=["GET"])
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
    response = employee_service.get_employees(payload)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return response, status_return

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


@employees.route("/<id>", methods=["GET"])
@requires_access_level(["READ"])
def get_by_id(id):
    response = employee_service.get_employee_by_id(id)

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


@employees.route("/update", methods=["PATCH"])
@requires_access_level(["READ", "WRITE", "UPDATE"])
def update():
    data = request.get_json()
    response = employee_service.update_employee(data, "employees")

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
            id : id of the employee that will be deleted
        }
     
    responses:
        status 200:
            description: Success
        status 400:
            description: Invalid
        status 403:
            description: Error permission
"""


@employees.route("/delete", methods=["DELETE"])
@requires_access_level(["READ", "WRITE", "UPDATE", "DELETE"])
def delete():
    response = employee_service.delete_employee(request.args)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )
