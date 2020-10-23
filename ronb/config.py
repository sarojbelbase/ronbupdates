from dotenv import find_dotenv, load_dotenv
from os import path, environ, sep, pardir

# basedir = path.abspath(path.dirname(__file__))
# rootdir = path.normpath(basedir + sep + pardir)
load_dotenv(find_dotenv())


class Configuration:

    SECRET_KEY = environ.get('SECRET_KEY')
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
    ACCESS_KEY = environ.get('ACCESS_KEY')
    ACCESS_SECRET = environ.get('ACCESS_SECRET')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    BOT_TOKEN = environ.get('BOT_TOKEN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
