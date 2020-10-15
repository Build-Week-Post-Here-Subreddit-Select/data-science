from flask import Flask, request, jsonify
from pathlib import Path
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Generic Return'
    return app