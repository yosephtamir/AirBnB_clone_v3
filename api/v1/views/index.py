#!/usr/bin/python3
"""A flask app to return a json file"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returning the API by jsonfying it """
    st = {
        'status': 'OK'
    }
    return jsonify(st)
