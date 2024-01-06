#!/usr/bin/python3
"""defining routes"""
from api.v1.views import app_views
from flask import jsonify, Response, request
from models import storage
import json


@app_views.route('/status', methods=['GET'])
def status():
    """return the status"""
    status = (
            '{\n'
            '  "status": "OK"\n'
            '}\n'
            )
    return Response(
            response=status,
            status=200,
            mimetype='application/json'
            )

@app_views.route('/stats', methods=['GET'])
def stats():
    """Returns count of all class objects."""
    if request.method == 'GET':
        response = {}
        PLURALS = {
                "Amenity": "amenities",
                "City": "cities",
                "Place": "places",
                "Review": "reviews",
                "State": "states",
                "User": "users"
        }
        
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
