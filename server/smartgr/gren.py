from dbmanager import dbmanager
from model import DataPacket,GroupDataModel
import packetmanager

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
            group = db.findGroupByQueries(datapacket.queries)
        else:
            words = GroupDataModel.Words(queries = datapacket.data)
            group = GroupDataModel.Group(words=words)
            group.ID = db.createGroup(group)
            
        db.joinUser(datapacket.ID.group.ID)
