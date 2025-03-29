from datetime import datetime, timedelta
from bson import ObjectId
from extensions import db

class Event:
    @staticmethod
    def create_event(data):
        """Create a new event document"""
        event = {
            'timestamp': datetime.utcnow(),
            'location': data.get('location', f"Camera-{ObjectId()}"),
            'people_count': data['count'],
            'density': data['count'] / 10,  # Assuming 10 sqm area per camera
            'anomalies': data['anomalies'],
            'detections': data['detections']
        }
        return db.events.insert_one(event)
    
    @staticmethod
    def get_recent_events(hours=24, limit=100):
        """Get events from last N hours"""
        time_threshold = datetime.utcnow() - timedelta(hours=hours)
        return list(db.events.find(
            {'timestamp': {'$gte': time_threshold}}
        ).sort('timestamp', -1).limit(limit))
    
    @staticmethod
    def get_stats(hours=1):
        """Get statistics from last N hours"""
        time_threshold = datetime.utcnow() - timedelta(hours=hours)
        
        pipeline = [
            {'$match': {'timestamp': {'$gte': time_threshold}}},
            {'$group': {
                '_id': None,
                'total_people': {'$sum': '$people_count'},
                'avg_density': {'$avg': '$density'},
                'active_locations': {'$addToSet': '$location'}
            }},
            {'$project': {
                '_id': 0,
                'total_people': 1,
                'avg_density': 1,
                'active_locations': {'$size': '$active_locations'}
            }}
        ]
        
        result = list(db.events.aggregate(pipeline))
        return result[0] if result else {
            'total_people': 0,
            'avg_density': 0,
            'active_locations': 0
        }