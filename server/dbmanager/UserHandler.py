import xml.sax
import xml.sax.xmlreader
import xml.sax.saxutils

import dbconfig

# **************************************************
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
# *************************************************

from model.User import User
from model.QueryData import QueryData

class UserHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.users = []
        self.queryData = None

    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "User": self.u = User()
        if tag == "Query": 
            self.queryData = QueryData()
            self.queryData.setRequestedTime(attributes['time'])


    def endElement(self,tag):
        if tag == "User":
            self.users.append(self.u)
        if tag == "Query": self.u.appendQuery(self.queryData)
        self.CurrentData = ""

    
    def characters(self,content):
        if self.CurrentData == "ID":
            self.u.ID = content

        if self.CurrentData == "FacebookID":
            self.u.facebookID = content

        if self.CurrentData == "Query":
            self.queryData.setQuery([x for x in content.split(" ")])

        if self.CurrentData == "Password":
            self.u.passwd = content


    def parse(self,f):
        xml.sax.parse(f,self)
        return self.users
        
def selelctByID(ID):
    users = UserHandler().parse(dbconfig.loadfile)
    
    for u in users:
        if u.ID == ID:
            return u

    return None


def save(users):
    f = open(dbconfig.userfile,'w')
    x = xml.sax.saxutils.XMLGenerator(f,'utf-8')
    attr0 = xml.sax.xmlreader.AttributesImpl({})
    x.startDocument()
    x.startElement("UserInformation")

    for u in users:
        x.startElement("User",attr0)

        x.startElement("ID",attr0)
        x.characters(u.ID)
        x.endElement("ID")

        x.startElement("FacebookID",attr0)
        x.characters(u.facebookID)
        x.endElement("FacebookID")

        x.startElement("Query",attr0)
        for q in u.query:
            x.characters(q + " ")
        x.endElement("Query")
            
        x.startElement("Password",attr0)
        x.characters(u.passwd)
        x.endElement("Password")

        x.endElement("User")

    x.endElement("UserInformation")


users =  UserHandler().parse(dbconfig.loadfile)

print "RESULT:"
print users[0]
print usres[1]
