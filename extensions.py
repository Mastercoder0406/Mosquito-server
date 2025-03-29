from flask_mqtt import Mqtt
from pymongo import MongoClient
from config import Config

mqtt = Mqtt()
mongo = MongoClient(Config.MONGO_URI)
db = mongo.get_database()