from pymongo import MongoClient
from config import settings

conn = MongoClient(settings.mongodb_uri, settings.port)
db = conn['courses']