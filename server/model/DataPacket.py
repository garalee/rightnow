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


# Packet For Intercommunication between Web Handler(Client) and Data Handler(Server)
# ID (4byte)
# #queries (4byte)
# #kewwords (4byte)
# queries (4*8byte) sending 8 queries at once
# keywords (4*64byte) sending 64 keywords at once

class DataPakcet:
    def __init__(self,ID,queries,keywords):
        self.ID = ID
        self.queries = queries
        self.keywords = keywords


    def getQueries(self):
        return self.queries

    def getKeywords(self):
        return self.keywords

