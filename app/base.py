from app.models.todo_model import ToDo
from flask import Blueprint, jsonify

base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/')
def hello_world():
    return 'Hello World!'


@base_blueprint.route('/get_todo')
def get_todo():
    query = ToDo.query.all()
    todo_dict = {}
    for todo in query:
        todo_dict.update({'id':todo.id, 'category': todo.category, 'description': todo.description})
    return jsonify({'data': todo_dict})