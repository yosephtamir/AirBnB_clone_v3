#!/usr/bin/python3
"""A flask app to return a json file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returning the API by jsonfying it """
    st = {
        'status': 'OK'
    }
    return jsonify(st)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    objectNames = ["amenities", "cities", "places", "reviews", "states", "users"]

    objects = {}
    for i in range(len(classes)):
        objects[objectNames[i]] = storage.count(classes[i])

    return jsonify(objects)