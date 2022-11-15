from flask import Flask
from src.app.controllers.user import users

def routes(app: Flask):
  app.register_blueprint(users)