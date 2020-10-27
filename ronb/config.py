from dotenv import find_dotenv, load_dotenv
from os import path, environ, sep, pardir

# basedir = path.abspath(path.dirname(__file__))
# rootdir = path.normpath(basedir + sep + pardir)
load_dotenv(find_dotenv())


class Configuration:

    CHANNEL = environ.get('CHANNEL')
    BOT_TOKEN = environ.get('BOT_TOKEN')
    ACCESS_KEY = environ.get('ACCESS_KEY')
    TWEETARATI = environ.get('TWEETARATI')
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    BOT_USERNAME = environ.get('BOT_USERNAME')
    ACCESS_SECRET = environ.get('ACCESS_SECRET')
    CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
