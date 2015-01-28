
class User:

    def __init__(self):
        self.query = []
        self.ID = 0
        self.facebookID = 0
        self.passwd = ""
        self.ipaddr = ""
    
    def appendQuery(self,query):
        self.query.append(query)
        
    def removeQuery(self,query):
        self.query.remove(query)


    def __str__(self):
        l = "ID : " + str(self.ID) + ",Facebook ID: " + str(self.facebookID) + "\n"

        for query in self.query:
            l += str(query)

        l += "Password : " + self.passwd + '\n'
        l += "IP address : " + self.ipaddr + '\n'
        return l
