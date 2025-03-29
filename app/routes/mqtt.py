from flask import Blueprint
import json
from ..extensions import mqtt, db
from ..models import CrowdEvent

mqtt_bp = Blueprint('mqtt', __name__)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('crowd/events')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    event = CrowdEvent(
        people_count=data['people_count'],
        location=data['location'],
        density=data['density']
    )
    db.session.add(event)
    db.session.commit()