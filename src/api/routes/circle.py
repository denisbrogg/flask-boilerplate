from flask import Blueprint, request, jsonify, make_response
import numpy as np
import json

circle_blueprint = Blueprint('circle_blueprint', __name__)

@circle_blueprint.route('/area', methods=['GET'])
def get_area():
    """Get all logs and compute metrics for the web dashboard
    """
    radius = request.args.get("radius", 1)
    return json.dumps({"area": float(radius)**2 * np.pi })