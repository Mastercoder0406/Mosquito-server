from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
mqtt = Mqtt()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)