from extensions import mqtt, db
from models.event import Event
import json

def init_mqtt(app):
    mqtt.init_app(app)
    
    @mqtt.on_connect()
    def handle_connect(client, userdata, flags, rc):
        app.logger.info(f"MQTT connected with result code {rc}")
        mqtt.subscribe(app.config['MQTT_TOPIC'])
    
    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        try:
            data = json.loads(message.payload.decode())
            app.logger.info(f"Received MQTT message: {data}")
            
            # Store in MongoDB
            Event.create_event(data)
            
        except Exception as e:
            app.logger.error(f"Error processing MQTT message: {e}")