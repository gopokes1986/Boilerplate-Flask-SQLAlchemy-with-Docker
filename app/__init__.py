from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_pyfile('app_config.py')
    return app


app = create_app()
db = SQLAlchemy(app)

from app.base import base_blueprint

app.register_blueprint(base_blueprint)
