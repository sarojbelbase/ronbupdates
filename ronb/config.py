import os

basedir = os.path.abspath(os.path.dirname(__file__))
rootdir = os.path.normpath(basedir + os.sep + os.pardir)


class Configuration:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_KEY = os.environ.get('ACCESS_KEY')
    ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
