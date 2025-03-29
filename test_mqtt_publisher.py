import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT Test Data Generator
def generate_test_data():
    return {
        "count": random.randint(0, 20),
        "anomalies": random.randint(0, 3),
        "detections": [[random.randint(0,100), random.randint(0,100), 
                      random.randint(100,200), random.randint(100,200)] 
                     for _ in range(random.randint(0, 5))]
    }

# MQTT Configuration
broker = "localhost"
topic = "crowd/edge_updates"

client = mqtt.Client()
client.connect(broker)

try:
    while True:
        test_data = generate_test_data()
        client.publish(topic, json.dumps(test_data))
        print(f"Published: {test_data}")
        time.sleep(2)  # Send data every 2 seconds
except KeyboardInterrupt:
    client.disconnect()