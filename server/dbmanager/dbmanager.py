from Dao import UserDao
from Dao import GroupDao
from Dao import UserJoinDao
from Dao import IPTableDao

from model import User

import multiprocessing
from multiprocessing import *

class DBManager:
	def __init__(self):
		self.userDao = UserDao.UserDao()
		self.groupDao = GroupDao.GroupDao()
		self.userJoinDao = UserJoinDao.UserJoinDao()
		self.iptableDao = IPTableDao.IPTableDao()
		self._semaphores = Semaphore(10)

# User Operations
	def createUser(self,user):
		self._semaphores.acquire()
		r = self.userDao.insertUser(user)
		self._semaphores.release()

		return r

	def findUserByID(self,ID):
		self._semaphores.acquire()
		r = self.userDao.selectUserByID(ID)
		self._semaphores.release()
		return r

	def findUserByFacebookID(self,facebookID):
		self._semaphores.acquire()
		r = self.userDao.selectUserByFacebookID(facebookID)
		self._semaphores.release()
		return r
	
	# Updating User
	def updateUser(self,user):
		self._semaphores.acquire()
		r = self.userDao.updateUser(user)
		self._semaphores.release()
		return r
		

	# Deleting User
	# It is easier to delete user after selecting a user by ID or facebookID
	# Return 1 if succeed to delete
	def deleteUser(self,user):
		self._semaphores.acquire()
		r = self.userDao.deleteUser(user)
		self._semaphores.release()
		return r


# Group Operations
	def createGroup(self,group):
		self._semaphores.acquire()
		words = self.groupDao.selectWordsByQueries(group.words.queries)
		self._semaphores.release()
		if  words== None:
			self._semaphores.acquire()
			wordsID = self.groupDao.insertWords(group.words)
		
			group.wordsID = wordsID

			r = self.groupDao.insertGroup(group)
			self._semaphores.release()
			return r
	
	def findGroupByQueries(self,queries):
		self._semaphores.acquire()
		words = self.groupDao.selectWordsByQueries(queries)
		self._semaphores.release()

		if words == None:
			return None
		else: 
			self._semaphores.acquire()
			r = self.groupDao.selectGroupByWordsID(words.ID)
			self._semaphores.release()
			return r
		

	# return True if given queries are already in the database
	# return False otherwise
	def groupExistsByQueries(self,queries):
		self._semaphores.acquire()
		r = self.groupDao.selectWordsByQueries(queries)
		self._semaphores.release()

		if r == None:
			return False
		return True

	# return 1 if given keywords are already in the database
	# return 0 otherwise
	def groupExistsByKeywords(self,keywords):
		self._semaphores.acquire()
		r = self.groupDao.selectWordsByKeywords(keywords)
		self._semaphores.release()
		if r == None:
			return False
		return True

	def joinUser(self,userID,groupID):
		self._semaphores.acquire()
		r = self.userJoinDao.joinGroup(groupID,userID)
		self._semaphores.release()
		return r

	def disjoinUser(self,userID,groupID):
		self._semaphores.acquire()
		r = self.userJoinDao.disjoinGroup(groupID,userID)
		self._semaphores.release()
		return r

	def getUserIDByGroupID(self,groupID):
		self._semaphores.acquire()
		userIDs = self.userJoinDao.selectUserByGroupID(groupID)
		self._semaphores.release()

		return userIDs

	def selectGroupByUserID(self,userID ):
		return self.groupDao.selectGroupByUserID(userID)

	def selectWordsByGroupID(self,groupID ):
		return self.groupDao.selectWordsByGroupID(groupID)


# IPTable Operation
	def insertIP(self,userID,ipaddr):
		self._semaphores.acquire()
		r = self.iptableDao.insert(userID,ipaddr)
		self._semaphores.release()
		return r

	def removeIP(self,userID,ipaddr):
		self._semaphores.acquire()
		r = self.iptableDao.delete(userID,ipaddr)
		self._semaphores.release()
		return r

	def getIPs(self,userID):
		self._semaphores.acquire()
		r = self.iptableDao.selectIPsByUserID(userID)
		self._semaphores.release()
		return r
