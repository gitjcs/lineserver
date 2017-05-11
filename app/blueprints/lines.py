from flask import Blueprint
from app.exceptions import InvalidParameterError
from db.lines_repository import LinesRepository

lines = Blueprint('lines', __name__)


@lines.route('/<line_index>', methods=['GET'])
def get_index(line_index):
    try:
        line_index = int(line_index)
    except ValueError:
        raise InvalidParameterError()

    # Sqlite is weird with threading, need to create a new
    # connection per request. With a real db wed create one
    # connection per app and reuse that
    return LinesRepository().get_line(line_index)
