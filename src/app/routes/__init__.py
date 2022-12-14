from flask import Flask

from src.app.controllers.employees import employees
from src.app.controllers.inventory import inventory
from src.app.controllers.user import users


def routes(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(employees)
    app.register_blueprint(inventory)
