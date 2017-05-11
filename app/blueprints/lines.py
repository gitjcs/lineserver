from flask import app, Blueprint

lines = Blueprint('lines', __name__)


@lines.route('/<line_index>', methods=['GET'])
def get_index(line_index):
    return app.lines_repo.get_line(line_index)
