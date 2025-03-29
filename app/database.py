from . import mongo
from datetime import datetime

class CrowdEvent:
    @staticmethod
    def create_event(data):
        event = {
            'timestamp': datetime.utcnow(),
            'people_count': data['people_count'],
            'location': data['location'],
            'density': data['density']
        }
        return mongo.db.events.insert_one(event)
    
    @staticmethod
    def get_recent_events(limit=100):
        return list(mongo.db.events.find().sort('timestamp', -1).limit(limit))