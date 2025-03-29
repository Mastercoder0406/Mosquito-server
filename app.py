from flask import Flask, jsonify, send_from_directory
from extensions import mqtt
from utils.mqtt_handler import init_mqtt
from config import Config

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    
    # Initialize MQTT
    init_mqtt(app)
    
    # API Routes
    @app.route('/')
    def serve_dashboard():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/api/events')
    def get_events():
        from models.event import Event
        events = Event.get_recent_events(hours=24)
        return jsonify(events)
    
    @app.route('/api/stats')
    def get_stats():
        from models.event import Event
        stats = Event.get_stats(hours=1)
        return jsonify(stats)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])