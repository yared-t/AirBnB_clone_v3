#!/usr/bin/python3xx
# Author: mikiasHailu and yared tsgie
''' This will show the api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def returnstuff():
    ''' This funciton will return stuff'''
    return jsonify(status='OK')

@app_views.route('/stats', strict_slashes=False)
def stuff():
    ''' This funciton is about the JSON Responses'''
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
