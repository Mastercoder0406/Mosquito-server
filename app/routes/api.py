from flask import Blueprint, jsonify, request
from ..extensions import db, limiter
from ..models import CrowdEvent

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/events', methods=['GET'])
@limiter.limit("100/hour")
def get_events():
    events = CrowdEvent.query.order_by(CrowdEvent.timestamp.desc()).limit(100).all()
    return jsonify([event.to_dict() for event in events])

@api_bp.route('/api/events', methods=['POST'])
@limiter.limit("100/hour")
def create_event():
    data = request.json
    event = CrowdEvent(
        people_count=data['people_count'],
        location=data['location'],
        density=data['density']
    )
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201