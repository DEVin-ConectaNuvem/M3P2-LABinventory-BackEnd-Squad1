import bcrypt 
from src.app import mongo_client
from src.app.utils import exist_key

class User():  
  def __init__(self, email, password, role):
    self.email = email
    self.password = password
    self.role = role

  def check_password(self, password):
    return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

  @classmethod
  def seed(cls, email, password, role):
    user = User(
      email = email,
      password = password,
      role = role
    )
    user.password = user.encrypt_password(password.encode("utf-8"))
    user.save()

  @staticmethod
  def encrypt_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

  def save(self):
    roles_query = mongo_client.roles.find_one({'name': self.role})

    mongo_client.users.insert_one(
      {
        "email": self.email,
        "password": self.password,
        "role": roles_query['_id']
      }
    )



def create_user(request_data):
  try:
    list_keys = ["email", "password"]
    roles = [ "ADMIN", "BACK_END", "FRONT_END", "FULLSTACK", "USER"]

    data = exist_key(request_data, list_keys)

    if "error" in data:
      return data

    exist_user = mongo_client.users.find_one({'email': data['email']})

    if exist_user:
      return {"error": "Usuário já existente!"}

    role = "USER"

    if "role" in data:
      if data['role'] in roles:
        role = data['role']


    User.seed( 
      data['email'], 
      data['password'],
      role
    )

    return {"message": "Usuário foi criado com sucesso."}
  except:
    return {"error": "Algo deu errado!"}