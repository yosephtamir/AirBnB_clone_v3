#!/usr/bin/python3
"""This is used to run the flask web app"""
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(error):
    """used to close the database after using it"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Make a response if there is no webpage found"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """This script runs if it is not imported"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host, port, threaded=True)
