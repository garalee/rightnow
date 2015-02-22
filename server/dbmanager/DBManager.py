from Dao import UserDao
from Dao import GroupDao
from Dao import UserJoinDao

from model import User


class DBManager:
    def __init__(self):
        self.userDao = UserDao.UserDao()
        self.groupDao = GroupDao.GroupDao()
        self.userJoinDao = UserJoinDao.UserJoinDao()

# User Operations
    def createUser(self,user):
        return self.userDao.insertUser(user)

    def findUserByID(self,ID):
        return self.userDao.selectUserByID(ID)

    def findUserByFacebookID(self,facebookID):
        return self.userDao.selectUserByFacebookID(facebookID)
    
    # Updating User
    def updateUser(self,user):
        return self.userDao.updateUser(user)

    # Deleting User
    # It is easier to delete user after selecting a user by ID or facebookID
    # Return 1 if succeed to delete
    def deleteUser(self,user):
        return self.userDao.deleteUser(user)


# Group Operations
    def createGroup(self,group):
        wordsID = self.groupDao.insertWords(group.words)
        group.wordsID = wordsID

        return self.groupDao.insertGroup(group)

    # return True if given queries are already in the database
    # return False otherwise
    def groupExistsByQueries(self,queries):
        if self.groupDao.selectWordsByQueries(queries) == None:
            return False

        return True

    # return 1 if given keywords are already in the database
    # return 0 otherwise
    def groupExistsByKeywords(self,keywords):
        if self.groupDao.selectWordsByKeywords(keywords) == None:
            return False
        return True

    def joinUser(self,user,group):
        return self.userJoinDao.joinGroup(group.ID,user.ID)

    def disjoinUser(self,user,group):
        return self.userJoinDao.disjoinGroup(group.ID,user.ID)


