from flask import Blueprint, jsonify, request
from ..database import CrowdEvent
from ..schemas import CrowdEventSchema
from bson import json_util
import json

bp = Blueprint('api', __name__)
schema = CrowdEventSchema()

@bp.route('/events', methods=['POST'])
def create_event():
    try:
        data = schema.load(request.json)
        event_id = CrowdEvent.create_event(data)
        return jsonify({"status": "success", "id": str(event_id.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/events', methods=['GET'])
def get_events():
    events = CrowdEvent.get_recent_events()
    return json.loads(json_util.dumps(events))