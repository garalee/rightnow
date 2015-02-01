
class User:
    def __init__(self):
        self.groups = []
        self.ID = 0
        self.facebookID = 0
        self.passwd = ""
        self.ipaddr = ""


    def __str__(self):
        l = "ID : " + str(self.ID) + ",Facebook ID: " + str(self.facebookID) + "\n"

        for query in self.query:
            l += str(query)

        l += "Password : " + self.passwd + '\n'
        l += "IP address : " + self.ipaddr + '\n'
        return l
