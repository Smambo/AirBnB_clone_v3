#!/usr/bin/python3
"""defining routes"""
from . import app_views
from flask import jsonify, Response
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
