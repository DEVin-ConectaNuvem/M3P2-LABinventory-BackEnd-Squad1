from src.app import app, mongo_client
from src.app.routes import routes
from src.app.models.roles import create_collection_roles
from src.app.models.users import create_collection_users
from src.app.models.employers import create_collection_employers
from flask.cli import with_appcontext
import click

routes(app)

@click.command(name='create_collections')
@with_appcontext 
def call_command():
  create_collection_roles(mongo_client)
  create_collection_users(mongo_client)
  create_collection_employers(mongo_client)


app.cli.add_command(call_command)

if __name__ == "__main__":
  app.run()