import dbconfig

import pymongo
from pymongo import MongoClient

class MongoConnector:
    def __init__(self):
        self.client = MongoClient(dbconfig.db_host,dbconfig.db_port)
        self.db = self.client[dbconfig.db_database]

    def getCollection(self,name):
        return self.db[name]

    def getDatabase(self):
        return self.db
