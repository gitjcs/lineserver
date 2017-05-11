"""
Entry point for the lineserver flask application
"""
import os
import sys
from flask import Flask, jsonify
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(_root)
from config import init_config, Config
from app.exceptions import IndexOutOfRangeException
from blueprints.lines import lines
from managers.lines_manager import LinesManager

app = Flask('lineserver')

# Initialize blueprints
app.register_blueprint(lines, url_prefix='/lines')


# Initialize error handlers
@app.errorhandler(IndexOutOfRangeException)
def error_413_handler(exc):
    return jsonify({'error': exc.__class__.__name__}), 413


# Init managers
app.lines_manager = LinesManager()

if __name__ == '__main__':
    print("Starting lineserver...")
    init_config()
    app.run(host=Config.API_HOST,
            port=Config.API_PORT,
            debug=True,
            use_debugger=True,
            use_reloader=True)
