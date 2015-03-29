from model import DataPacket
from model import ChatPacket
#1from struct import pack,unpack
import pickle


class PacketManager:
	__flag_map = {"QUERY_DATA" : 0,
				  "KEYWORD_DATA": 1,
				  "CHAT_ROOM": 2}

	# Packet For Intercommunication between Web Handler(Client) and Data Handler(Server)
	# ID (4byte)
	# Flag (4byte)
	# #queries (4byte)
	# #kewwords (4byte)
	# queries (16*8byte) sending 8 queries at once
	# keywords (4*64byte) sending 64 keywords at once

	@staticmethod
	def datapack(datapacket):
		return pickle.dumps( datapacket )


	@staticmethod
	def dataunpack(packed):
		datapacket = pickle.loads( packed )
		return datapacket

	@classmethod
	def isquery(self, datapacket):
		if datapacket.flag == self.__flag_map['QUERY_DATA']: return True
		else: return False


	
	# Packet For Intercommunication between Chat Handler(Client) and Chat Manager(Server)
	# ID (4 bytes) user ID
	# groupID (4 bytes) group ID a user joined
	# message (248) message

	@staticmethod
	def chatpack(chatpacket):
		p = pack('I',chatpacket.ID)
		p += pack('I',chatpacket.groupID)
		p += pack('248s',chatpacket.msg)

		return p

	@staticmethod
	def chatunpack(packed):
		chatpacket = ChatPacket.ChatPacket()
		chatpacket.ID = unpack('I',packed[0:4])
		packed = packed[4:]
		chatpacket.groupID = unpack('I',packed[0:4])
		packed = packed[4:]

		datapcket.msg = unpack('252s',packed).split('\x00')

		return chatpacket
