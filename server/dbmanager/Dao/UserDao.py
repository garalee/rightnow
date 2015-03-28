from dbmanager.Dao import DB
from model import User
from bson.objectid import ObjectId


class UserDao:
    def selectUserByID(self,ID):
        user_collection = DB.User
        a = user_collection.find({"_id":ObjectId(ID)})
        u = None

        for i in a:
            u = User.User()
            u.passwd = i['password']
            u.facebookID = i['facebookID']
            u.ID = i['_id']

        return u

    def selectUserByFacebookID(self,facebookID):
        user_collection = DB.User
        a = user_collection.find({"facebookID" : facebookID})
        u = None
        for i in a:
            u = User.User()
            u.passwd = i['password']
            u.facebookID = i['facebookID']
            u.ID = i['_id']

        return u

    def deleteUser(self,user):
        user_collection = DB.User
        a = user_collection.remove({"_id":ObjectId(user.ID)})
        return a['ok']

    def insertUser(self,user):
        dbuser = {}
        dbuser['facebookID'] = user.facebookID
        dbuser['password'] = user.passwd

        user_collection = DB.User
        result = user_collection.insert(dbuser)
        return result
        

    def updateUser(self,user):
        user_collection = DB.User
        result = user_collection.update({'_id' : ObjectId(user.ID)}, {'$set' : 
                                                  {'facebookID': user.facebookID,
                                                   'password' : user.passwd}},
                               upsert=False)
        return result['updatedExisting']
        
