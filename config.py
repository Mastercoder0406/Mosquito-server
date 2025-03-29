import os

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/crowd_monitoring")
    MQTT_BROKER_URL = os.getenv("MQTT_BROKER_URL", "localhost")
    MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")