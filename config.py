import os

class Config:
    # MQTT Configuration
    MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'localhost')
    MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', 1883))
    MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'crowd/edge_updates')
    
    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/crowd_monitoring')
    
    # Server Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'