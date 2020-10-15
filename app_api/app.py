from flask import Flask #, request, jsonify
#from pathlib import Path
from flask_cors import CORS #, cross_origin
import json

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'Generic Return'

    @app.route('/predict', methods=['POST'])
    def predict_sub():

        return(json.dumps({'input':'test', 'predict':'r/AdviceAnimals'}))

    return app