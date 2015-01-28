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
