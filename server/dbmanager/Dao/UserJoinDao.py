from dbmanager.Dao import DB
from model import GroupDataModel
from model import User


class UserJoinDao:
    def joinGroup(self,groupID,userID):
        gJoin = {}
        gJoin['groupID'] = groupID
        gJoin['userID'] = userID

        userJoin_collection = DB.UserJoin
        return userJoin_collection.insert(gJoin)
        

    def disjoinGroup(self,groupID,userID):
        userJoin_collection = DB.UserJoin

        gJoin = {}
        gJoin['groupID'] = groupID
        gJoin['userID'] = userID

        a = userJoin_collection.remove(gJoin)
        return a['ok']

    def selectUserByGroupID(self,groupID):
        userJoin_collection = DB.UserJoin
        userIDs = []

        a = userJoin_collection.find({"groupID":groupID})
        for i in a:
            userIDs.append(i['userID'])

        return userIDs
