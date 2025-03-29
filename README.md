# Crowd Monitoring Server

A Flask-based web application for receiving and displaying crowd monitoring data from edge devices.

## Features

- Real-time data reception via MQTT and HTTP API
- SQLite database for persistent storage
- Interactive dashboard with charts and statistics
- Rate limiting for API protection
- Real-time updates via polling

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the MQTT broker (Mosquitto):
   ```bash
   sudo service mosquitto start
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

## API Endpoints

- `GET /api/events`: Retrieve crowd events
- `POST /api/events`: Create a new crowd event

## MQTT Topics

- `crowd/events`: Subscribe to receive crowd event data

## Data Format

```json
{
  "people_count": 50,
  "location": "Main Entrance",
  "density": 0.75
}
```