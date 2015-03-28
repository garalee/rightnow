from dbmanager import dbmanager
from model import DataPacket, GroupDataModel, User
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

		user = self.db.findUserByFacebookID( datapacket.ID[0] )
		self.db.joinUser(user.ID, group.ID)


	def getUserInfo( self, username, IPaddr ):

		user = self.db.findUserByFacebookID( username )
		if user == None:
			tempuser = User.User(facebookID=username,passwd="...")
			userID = self.db.createUser(tempuser)
			user = self.db.findUserByID(userID)

		ips = self.db.getIPs( user.ID )
		if ips != None:
			self.db.removeIP( user.ID, IPaddr )
		print 'getUserInfo', username, user.ID
		self.db.insertIP( user.ID, IPaddr )
		return user
