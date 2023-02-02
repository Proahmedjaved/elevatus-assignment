"""
This module contains the database connection.
"""

from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_CONNECTION_STRING)
# Database
db = client[settings.MONGO_DB_NAME]

# Collections
users = db['users']
candidates = db['candidates']
