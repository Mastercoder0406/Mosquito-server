class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///crowd_data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MQTT_BROKER_URL = 'localhost'
    MQTT_BROKER_PORT = 1883
    MQTT_KEEPALIVE = 60
    MQTT_TLS_ENABLED = False