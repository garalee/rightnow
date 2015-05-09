import socket
from rightnow_logger import Log
from config import RightnowConfig
from model import DataPacket
from smartgr import gren

import pickle
from dbmanager import dbmanager
from PacketManager import PacketManager as pm

MAX_DATA_SIZE_FROM_CLIENT = 256	  # Maximum bytes received from Client

class DataManager:
	def __init__(self):
		self.sgr = gren.SGR()
		self.db = dbmanager.DBManager()

	def socket_init(self):
		try:
			self.data_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			self.dataTochat_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

			self.data_socket.bind((RightnowConfig.DATA_SERVER_IP,RightnowConfig.DATA_SERVER_PORT))
			self.dataTochat_socket.bind((RightnowConfig.DATA_TO_CHAT_IP,RightnowConfig.DATA_TO_CHAT_PORT))

		except socket.error, msg:
			Log.error(msg)

			self.data_socket.close()
			self.dataTochat_socket.close()
			return -1

		return 0

	def connecting_chat(self):
		try:
			self.dataTochat_socket.listen(1)
			(self.cs,sockname) = self.dataTochat_socket.accept()
		except socket.error,msg:
			Log.error(msg)
			return -1
		return 0

	def run(self):
		print "Succeed to Run(Data)"
		while True:
			try:
				(data,address) = self.data_socket.recvfrom(MAX_DATA_SIZE_FROM_CLIENT)
				rcvdatapacket = pm.dataunpack(data)
				rcvdatapacket.address = address

				user = self.sgr.getUserInfo( rcvdatapacket.ID[0], address )

				if pm.isquery( rcvdatapacket ) == True:
					#1self.sgr.runSGR(rcvdatapacket)
#s					self.sgr.queryMatching( rcvdatapacket )
					self.sgr.insertQuery( user, rcvdatapacket )
				else:
					# Get Queries Of Group By FacebookID
					#1user = self.d.findUserByFacebookID( objrcv.username[0] )
					#%print 'user.ID; ',user.ID
					"""
					group = self.db.selectGroupByUserID( user.ID )

					dp = []

					for gg in group:
						#%print 'gg.groupID: ',gg.groupID
						words = self.db.selectWordsByGroupID( gg.groupID )
						dp.append( DataPacket.DataPacket(gg.groupID, 2, words.queries) )

					self.data_socket.sendto( pickle.dumps(dp), address )
					"""

					dp = []

					wordsSet = self.sgr.getChatGroupByQueries(user)

					for ws in wordsSet:
						print '=============\nws.group_id ws.queries'
						print ws.group_id, ws.queries
						dp.append( DataPacket.DataPacket(ws.group_id, 2, ws.queries) )


					# sending data result to client
					self.data_socket.sendto( pickle.dumps(dp), address )

			except socket.error,msg:
				Log.error(error)
				Log.info("Program Exit")
				break
		
			
if __name__ == "__main__":
	d = DataManager()

	# Setting Logger
	logger_name = RightnowConfig.LOGGER_NAME_CHAT
	log_filepath = RightnowConfig.LOG_FILE_PATH_CHAT
	from rightnow_logger import Log
	Log.init(logger_name = logger_name,log_filepath=log_filepath)

	Log.info("Starting Server...")
	if d.socket_init() == -1:
		Log.error("Socket Init Failed : Program Exited")
		exit(-1)

	Log.info("Data Socket Initialized")
	Log.info("Wait For Chatting Manager...")
	if d.connecting_chat() == 0:
		Log.debug("DataToChat Socket Connected")

	d.run()
