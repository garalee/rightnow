
class User:
    def __init__(self,ID='',facebookID='',passwd=''):
        self.groups = []
        self.ID = ID
        self.facebookID = facebookID
        self.passwd = passwd
        self.ipaddr = ""


    def __str__(self):
        l = "ID : " + str(self.ID) + ",Facebook ID: " + str(self.facebookID) + "\n"

        l += "Password : " + self.passwd + '\n'
        return l
