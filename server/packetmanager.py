from model import DataPacket
from struct import pack,unpack


# Packet For Intercommunication between Web Handler(Client) and Data Handler(Server)
# ID (4byte)
# Flag (4byte)
# #queries (4byte)
# #kewwords (4byte)
# queries (16*8byte) sending 8 queries at once
# keywords (4*64byte) sending 64 keywords at once

class PakcetManager:
    __flag_map = {"QUERY_DATA" : 0,
                  "KEYWORD_DATA": 1}
    @staticmethod
    def pack(datapacket):
        p = pack('III',datapacket.ID,datapacket.flag,datapacket.data_len)

        for i in datapacket.data:
            p += pack('16s',i)
        
        return p

    @staticmethod
    def unpack(packed):
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
