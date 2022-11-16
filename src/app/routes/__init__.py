from flask import Flask
from src.app.controllers.user import users
from src.app.controllers.employers import employers
from src.app.controllers.inventory import inventory


def routes(app: Flask):
  app.register_blueprint(users)
  app.register_blueprint(employers)
  app.register_blueprint(inventory)