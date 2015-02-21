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
        pass
