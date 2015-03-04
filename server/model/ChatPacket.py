# Packet For Intercommunication between Chat Handler(Client) and Chat Manager(Server)
# ID (4 bytes) user ID
# message (252) message


class ChatPacket:
    def __init__(self,ID=0,groupID=0,msg = "",address=""):
        self.ID = ID
        self.msg = msg
        self.groupID = groupID
        self.address = address

    def __str__(self):
        return "ID: " + str(self.ID) + ",flag:" + str(self.msg)  + ",msg : " + self.address
