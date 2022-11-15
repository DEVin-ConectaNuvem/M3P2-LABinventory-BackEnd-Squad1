from flask import Flask
from src.app.controllers.user import users
from src.app.controllers.employers import employers

def routes(app: Flask):
  app.register_blueprint(users)
  app.register_blueprint(employers)