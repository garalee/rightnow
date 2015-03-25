from dbmanager import dbmanager
from model import DataPacket, GroupDataModel
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
		
			
	def queryMatching(self,datapacket):
		if self.db.groupExistsByQueries(datapacket.data):
			group = self.db.findGroupByQueries(datapacket.data)
		else:
			words = GroupDataModel.Words(queries = datapacket.data)
			group = GroupDataModel.Group(words=words)
			group.ID = self.db.createGroup(group)
			
		self.db.joinUser(datapacket.ID, group.ID)


	def getUserInfo( self, username, IPaddr ):
		print 'getUserInfo', username

		user = self.db.findUserByFacebookID( username )
		print 'getUserInfo222', username
		if user == None:
			tempuser = User.User(facebookID=username,passwd="...")
			userID = self.db.createUser(tempuser)
			user = self.db.findUserByID(userID)

		print 'getUserInfo333', username
		ips = self.db.getIPs( username )
		if ips != None:
			self.db.removeIP( username, IPaddr )
		print 'getUserInfo444', username
		self.db.insertIP( username, IPaddr )
		print 'getUserInfo555', username
		return user
