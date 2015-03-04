from model import DataPacket
from model import ChatPacket
from struct import pack,unpack


class PakcetManager:
    __flag_map = {"QUERY_DATA" : 0,
                  "KEYWORD_DATA": 1}

    
    # Packet For Intercommunication between Web Handler(Client) and Data Handler(Server)
    # ID (4byte)
    # Flag (4byte)
    # #queries (4byte)
    # #kewwords (4byte)
    # queries (16*8byte) sending 8 queries at once
    # keywords (4*64byte) sending 64 keywords at once

    @staticmethod
    def datapack(datapacket):
        p = pack('III',datapacket.ID,datapacket.flag,datapacket.data_len)

        for i in datapacket.data:
            p += pack('16s',i)
        
        return p

    @staticmethod
    def dataunpack(packed):
        datapacket = DataPacket.DataPacket()
        datapacket.ID = unpack('I',packed[0:4])
        packed = packed[4:]
        datapacket.flag = unpack('I',packed[0:4])
        packed = packed[4:]
        datapacket.data_len = unpack('I',packed[0:4])
        packed = packed[4:]

        for i in range(datapacket.data_len):
            datapacket.data.append(unpack('16s',p[0:16]).split('\x00'))
            packed = packed[16:]

        return datapacket

    @staticmethod
    def isquery(datapacket):
        if datapacket.flag == pm.__flag_map['QUERY_DATA']: return True
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
