from flask import Flask
from .extensions import db, mqtt, limiter
from .routes.api import api_bp
from .routes.mqtt import mqtt_bp

def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)
    mqtt.init_app(app)
    limiter.init_app(app)

    # Register blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(mqtt_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app