from flask import Flask
from flask_cors import CORS
import json

def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'Generic Return'

    # @app.route('/predict', methods=['POST'])
    # def predict_sub():

    #     return(json.dumps({'input':'test', 'predict':'r/AdviceAnimals'}))

    return app