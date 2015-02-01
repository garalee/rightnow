import socket

from rightnow.rightnow_log import Log


CHAT_SERVER_PORT = 12314
DATA_SERVER_PORT = 12356
CHAT_SERVER_IP = 'localhost'
DATA_SERVER_IP = 'localhost'
MAX_SIZE_FROM_CLIENT = 1024


class DataCenter:
    def __init__(self):
        pass

    def gr1_0(self,queries,keywords):
        pass

    def socket_init(self):
        try:
            self.data_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.chat_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            self.data_socket.bind((config.DATA_SERVER_IP,config.DATA_SERVER_PORT))
            self.chat_socket.bind((config.CHAT_SERVER_IP,config.CHAT_SERVER_PORT))

        except socket.error, msg:
            Log.error(msg)

            self.data_socket.close()
            self.chat_socket.close()
            return -1
            

        return 0

    def connecting_chat(self):
        self.chat_socket.listen(1)
        (self.cs,sockname) = self.chat_socket.accept()
        
        Log.info("Successfully Connected to Chat Handler")

    def run(self):
        while True:
            (data,address) = self.data_socket.recvfrom(MAX_SIZE_FROM_CLIENT)
            
            
            
if __name__ == "__main__":
    dc = DataCenter()

    if dc.socket_init() == -1:
        Log.error("Program Exited")
        exit(-1)

    
    Log.info("Socket Successfully Initialized")
    Log.info("Wait For Chatting Handler...")
    dc.connecting_chat()

    dc.run()
