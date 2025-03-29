from flask import Blueprint
from flask_mqtt import Mqtt
from ..database import CrowdEvent
from ..schemas import CrowdEventSchema
import json

bp = Blueprint('mqtt', __name__)
schema = CrowdEventSchema()

@bp.route('/init_mqtt')
def init_mqtt():
    mqtt.subscribe('crowd/events')
    return "MQTT Initialized", 200

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    try:
        data = schema.load(json.loads(message.payload))
        CrowdEvent.create_event(data)
    except Exception as e:
        print(f"MQTT Error: {str(e)}")