from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import json

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crowd_data.db'
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 60

# Initialize extensions
db = SQLAlchemy(app)
mqtt = Mqtt(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Database Models
class CrowdEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    people_count = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    density = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'people_count': self.people_count,
            'location': self.location,
            'density': self.density
        }

# Create database tables
with app.app_context():
    db.create_all()

# MQTT Subscription
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

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/events', methods=['GET'])
@limiter.limit("100/hour")
def get_events():
    events = CrowdEvent.query.order_by(CrowdEvent.timestamp.desc()).limit(100).all()
    return jsonify([event.to_dict() for event in events])

@app.route('/api/events', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)