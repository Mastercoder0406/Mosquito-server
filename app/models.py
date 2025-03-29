from datetime import datetime
from .extensions import db

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