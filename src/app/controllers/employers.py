from src.app.services import employers as employers_service
from flask import Blueprint, request
from flask.wrappers import Response
from bson import json_util

employers = Blueprint("employers", __name__, url_prefix="/employers")
employersService = employers_service.EmployersService()

@employers.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = employersService.create_employer(data)
    print(response)
    return Response(json_util.dumps(response), mimetype="application/json")


@employers.route("/find", methods=["GET"])
def get_find():
    data = request.get_json()
    response = employersService.get_employer(data)
    return Response(json_util.dumps(response), status=200, mimetype="application/json")


@employers.route("/", methods=["GET"])
def get_all():
    response = employersService.get_employers()
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employers.route("/getid", methods=["GET"])
def get_by_id():
    data = request.get_json()
    response = employersService.get_employer_by_id(data)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employers.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = employersService.update_employer(data)
    print(response)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employers.route("/delete", methods=["DELETE"])
def delete():
    response = employersService.delete_employer(request.args)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )