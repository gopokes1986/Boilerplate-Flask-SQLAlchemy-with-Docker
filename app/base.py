from app import app
from flask import Blueprint

base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/')
def hello_world():
    return 'Hello World!'
