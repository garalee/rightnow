from dbmanager import dbmanager
from model import DataPacket, GroupDataModel, User
from Util import returnRId
from sim import getMaxMatching
import PacketManager

class SGR:
	def __init__(self):
		self.db = dbmanager.DBManager()

	
	def runSGR(self,datapacket):
		if pm.isquery(datapacket) == True:
			ips = self.db.getIPs(datapacket.ID)
			if ips == None:
				self.db.insertIP(datapacket.ID,datapacket.address)
				
			self.queryMatching(datapacket)


	def getUserInfo( self, username, IPaddr ):

		user = self.db.findUserByFacebookID( username )
		if user == None:
			tempuser = User.User(facebookID=username,passwd="...")
			userID = self.db.createUser(tempuser)
			user = self.db.findUserByID(userID)

		ips = self.db.getIPs( user.ID )

		if ips != None:
			self.db.removeIP( user.ID, IPaddr )

#10		print 'getUserInfo', username, user.ID
		self.db.insertIP( user.ID, IPaddr )

		return user


	def queryMatching(self,datapacket):
		if self.db.groupExistsByQueries(datapacket.data):
			group = self.db.findGroupByQueries(datapacket.data)
		else:
			words = GroupDataModel.Words(queries = datapacket.data)
			group = GroupDataModel.Group(words=words)
			group.ID = self.db.createGroup(group)

		user = self.db.findUserByFacebookID( datapacket.ID[0] )
		self.db.joinUser(user.ID, group.ID)


	def insertQuery(self, user, datapacket):
		self.db.insertQueries(user.ID, datapacket)

	# return the user list with group_id and query set that has most similarity
	def getChatGroupByQueries(self, user):
		# Bring current user query sets
		curSet = self.db.getWordsByUserID(user.ID)

		# Bring others'query sets except current user
		totalSet = self.db.getOthersWordsByUserID(user.ID)

		# Run the algorithm for comparing similarity
		# - compare curUser with others[0:]
		# Find the most similar user
		print curSet
		print totalSet
		threshold = 50
		mKey, mIdx = getMaxMatching(curSet, totalSet, threshold)
		if mKey == None:
			wordsSet = []
			return wordsSet
#10		print mKey, mIdx
#10		print totalSet[mKey][mIdx[1]]

		# Insert these users into Group document with Group ID and Proper title( query which has the most similarity )
		groupSet = self.makeGroupSet(user.ID, curSet, totalSet, mKey, mIdx)

		# Return titles to user
		wordsSet = self.db.insertGroup(groupSet)

#10		print 'gren.py'
#10		print wordsSet
		return wordsSet


	def makeGroupSet(self, userId, curSet, totalSet, mKey, mIdx):
		groupSet = []

#10		print "Cur set"
#10		print curSet
#10		print "Tot set"
#10		print (totalSet[mKey][mIdx[1]]).queries

		tot1 = (totalSet[mKey][mIdx[1]]).queries
#		print tot1
		cur = []
		for cu in curSet:
			for c in cu.queries:
				cur.append(c)

		commons = []
		for a in tot1:
			if a in cur:
				if a not in commons:
					commons.append(a)

#		print commons


		groupID = returnRId('GID')
		groupSet.append(groupID)	# Group ID

		groupSet.append(commons)	# Common Queries

		groupSet.append(userId)
		groupSet.append(mKey)

		return groupSet



	"""
	def temp(self, cur, totalSet):
		cgroup = []
		cgroup.append(cur)

		tkeys = totalSet.keys()

		i = 0
		for tkey in tkeys:
			if i != 0:
				cgroup.append(totalSet[tkey])
			i = 1

		return cgroup

	def makeGroupSet(self, datas):
		cqueries = None
		groupSet = []

		groupID = returnRId('GID')
		groupSet.append(groupID)

		for data in datas:
			for mos in data:
				groupSet.append(mos.queries)
				break
			break

		previousUser = ''
		for data in datas:
			for mos in data:
				if previousUser != mos.user_id:
					groupSet.append(mos.user_id)
					previousUser = mos.user_id

		return groupSet
	"""



