import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Development(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = ""
    MONGO_URI = os.getenv("MONGO_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv("OAUTHLIB_INSECURE_TRANSPORT")
    BACKEND_URL = os.getenv("BACKEND_URL")
    FRONTEND_URL = os.getenv("FRONTEND_URL")


class Testing(object):
    DEBUG = False
    TESTING = True
    DATABASE_URI = ""
    MONGO_URI = os.getenv("MONGO_URI_TESTING")
    SECRET_KEY = os.getenv("SECRET_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv("OAUTHLIB_INSECURE_TRANSPORT")
    BACKEND_URL = os.getenv("BACKEND_URL")
    FRONTEND_URL = os.getenv("FRONTEND_URL")


class Production(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""
    SECRET_KEY = os.getenv("SECRET_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv("OAUTHLIB_INSECURE_TRANSPORT")
    BACKEND_URL = os.getenv("BACKEND_URL")
    FRONTEND_URL = os.getenv("FRONTEND_URL")


app_config = {"development": Development, "testing": Testing, "production": Production}
