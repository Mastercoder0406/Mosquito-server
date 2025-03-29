import pytest
from app import create_app
from app.database import CrowdEvent
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['MONGODB_URI'] = "mongodb://localhost:27017/crowd_monitoring_test"
    with app.test_client() as client:
        yield client
    # Cleanup test database
    CrowdEvent.mongo.db.events.drop()

def test_create_event(client):
    test_data = {
        "people_count": 10,
        "location": "Test Location",
        "density": 0.5
    }
    response = client.post('/events', json=test_data)
    assert response.status_code == 201
    assert "id" in response.json

def test_get_events(client):
    # Insert test data
    with open('tests/test_data.json') as f:
        test_data = json.load(f)
    for event in test_data:
        CrowdEvent.create_event(event)
    
    response = client.get('/events')
    assert response.status_code == 200
    assert len(response.json) == 2