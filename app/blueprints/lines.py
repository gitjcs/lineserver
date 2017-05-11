from flask import Blueprint, current_app
from app.exceptions import InvalidParameterError

lines = Blueprint('lines', __name__)


@lines.route('/<line_index>', methods=['GET'])
def get_index(line_index):
    try:
        line_index = int(line_index)
    except ValueError:
        raise InvalidParameterError()

    return current_app.lines_manager.get_line(line_index)
