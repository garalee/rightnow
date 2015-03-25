import socket
from rightnow_logger import Log
from config import RightnowConfig
from model import ChatPacket

MAX_CHAT_SIZE_FROM_CLIENT=256

class ChatManager:
    def socket_init(self):
        try:
            self.chat_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.chatTodata_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            self.chat_socket.bind((RightnowConfig.CHAT_SERVER_IP,RightnowConfig.CHAT_SERVER_PORT))
            self.chatTodata_socket.bind((RightnowConfig.CHAT_TO_DATA_IP,RightnowConfig.CHAT_TO_DATA_PORT))

        except socket.error, msg:
            Log.error(msg)
            
            self.data_socket.close()
            self.chatTodata_socket.close()
            return -1

        return 0

    def connecting_data(self):
        try:
            self.chatTodata_socket.connect((RightnowConfig.DATA_TO_CHAT_IP,RightnowConfig.DATA_TO_CHAT_PORT))
        except socket.error, msg:
            Log.error(msg)

            self.chatTodata_socket.close()
            self.chat_socket.close()
            return -1

        return 0

    def run(self):
        print "Succeed to Run(Chat)"
        while True:
            try:
                (data,address) = self.chat_socket.recvfrom(MAX_CHAT_SIZE_FROM_CLIENT)
                chatpacket = pm.chatunpack(data)
                chatpacket.address = address
                
                userIDs = self.db.getUserIDByGroupID(chatpacket.groupID)
                ips = []

                for i in userIDs:
                    ips.append(self.db.getIPs(i))

                # Sending Message To The Group
                for i in ips:
                    # send
                    pass
                break
            except socket.error,msg:
                Log.error(msg)
                Log.info("Program Exit")
                break

if __name__ == "__main__":
    c = ChatManager()


    # Setting Logger
    logger_name = RightnowConfig.LOGGER_NAME_DATA
    log_filepath = RightnowConfig.LOG_FILE_PATH_DATA
    from rightnow_logger import Log
    Log.init(logger_name=logger_name,log_filepath=log_filepath)

    Log.info("Starting Server...")
    if c.socket_init() == -1:
        Log.info("Socket Init Failed : Program Exited")
        exit(-1)
    
    Log.info("Chat Socket Initialized")
    Log.info("Connecting To Data Manager")
    if c.connecting_data() == 0:
        Log.debug("ChatToData Socket Connected")

    c.run()
