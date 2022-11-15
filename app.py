from src.app import app, mongo_client
from src.app.routes import routes

from flask.cli import with_appcontext
import click

routes(app)

if __name__ == "__main__":
  app.run()