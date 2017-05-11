from flask import Flask, jsonify
from blueprints.lines import lines
from exceptions import IndexOutOfRangeException
from db.lines_repository import LinesRepository

app = Flask('lineserver')

# Initialize blueprints
app.register_blueprint(lines, url_prefix='/lines')


# Initialize error handlers
@app.errorhandler(IndexOutOfRangeException)
def error_413_handler(exc):
    return jsonify({'error': exc.__class__.__name__}), 413


@app.errorhandler(Exception)
def generic_error(exc):
    return jsonify({'error': exc.__class__.__name__}), 500


# Initialize lines repo so we dont re-create a new connection
# to the sqlite db on every call
app.lines_repo = LinesRepository()
