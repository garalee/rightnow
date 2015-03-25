# Packet For Intercommunication between Web Handler(Client) and Data Handler(Server)
# ID (4byte)
# Flag (4byte)
# #queries (4byte)
# #kewwords (4byte)
# queries (16*8byte) sending 8 queries at once
# keywords (4*64byte) sending 64 keywords at once

class DataPacket:
    def __init__(self,ID=0,flag=0,data=[]):
        self.ID = ID
        self.flag = flag
        self.data = data
        self.data_len = len(data)
        self.address = ""


    def __str__(self):
        return "ID : " + str(self.ID) + ",flag:" + str(self.flag) + ",len: " + str(self.data_len) + ",query:" + str(self.data)


class QueryData:
	def __init__(self,query=None,requestedTime=None):
		if query == None: self.query = []
		else: self.query = query
		self.requestedTime = requestedTime
	
	def setRequestedTime(self,requestedTime):
		self.requestedTime = requestedTime

	def setQuery(self,*query):
		self.query = query

	def appendWord(self,q):
		self.query.append(q)

	def __str__(self):
		return "Query: " + str(self.query) + "Requested Time : " + str(self.requestedTime) + "\n"
