from dbmanager.Dao import DB
from model import User

import datetime

class IPTableDao:
    def insert(self,userID,ipaddr):
        ip_collection = DB.IPTable
        return ip_collection.insert({"ipaddr":ipaddr,"userID":userID,"expired" : datetime.datetime.now()})

    def delete(self,userID,ipaddr):
        ip_collection = DB.IPTable
        a = ip_collection.remove({"ipaddr" : ipaddr,"userID":userID})
        return a['ok']

    def selectIPsByUserID(self,userID):
        ip_collection = DB.IPTable
        a = ip_collection.find({"userID":userID})

        ips = []
        for i in a:
            ips.append((i['ipaddr'],i['expired']))

        return ips

    def selectExpired(self,userID,ipaddr):
        ip_collection = DB.IPTable
        a = ip_collection.find({"userID":userID,"ipaddr":ipaddr})
        expired = None
        for i in a:
            expired = i['expired']

        return expired
