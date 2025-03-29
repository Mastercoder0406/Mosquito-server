from flask import Flask
from flask_pymongo import PyMongo
from flask_mqtt import Mqtt
from .routes import api, mqtt_routes

mongo = PyMongo()
mqtt = Mqtt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    mongo.init_app(app)
    mqtt.init_app(app)
    
    # Register blueprints
    app.register_blueprint(api.bp)
    app.register_blueprint(mqtt_routes.bp)
    
    return app