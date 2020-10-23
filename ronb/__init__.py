from flask import Flask
from ronb.config import Configuration
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)

    from ronb.main.views import main
    app.register_blueprint(main)
    return app
