from pymongo import MongoClient
from datetime import datetime
import uuid

class DBManager:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client['twitter_trends']
        self.collection = self.db['trends']

    def insert_trends(self, trends, ip_address):
        document = {
            "_id": str(uuid.uuid4()),
            "date": datetime.now(),
            "ip_address": ip_address,
            "nameoftrend1": trends[0],
            "nameoftrend2": trends[1],
            "nameoftrend3": trends[2],
            "nameoftrend4": trends[3],
            "nameoftrend5": trends[4]
        }
        self.collection.insert_one(document)
        return document

# Usage:
# db_manager = DBManager('mongodb://localhost:27017/')
# db_manager.insert_trends(trends, ip_address)