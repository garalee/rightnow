from dbmanager.Dao import DB
from model import GroupDataModel
from model import User


class UserJoinDao:
    def joinGroup(self,groupID,userID):
        gJoin = {}
        gJoin['groupID'] = groupID
        gJoin['userID'] = userID

        groupJoin_collection = DB.User
        return groupJoin_collection.insert(gJoin)
        

    def disjoinGroup(self,groupID,userID):
        groupJoin_collection = DB.User

        gJoin = {}
        gJoin['groupID'] = groupID
        gJoin['userID'] = userID

        a = groupJoin_collection.remove(gJoin)
        return a['ok']
