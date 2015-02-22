import socket
from rightnow_logger import Log

from config import RightnowConfig

class DataManager:
    def socket_init(self):
        try:
            self.data_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.dataTochat_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            self.data_socket.bind((RightnowConfig.DATA_SERVER_IP,RightnowConfig.DATA_SERVER_PORT))
            self.dataTochat_socket.bind((RightnowConfig.DATA_TO_CHAT_SERVER_IP,RightnowConfig.DATA_TO_CHAT_SERVER_PORT))

        except socket.error, msg:
            Log.error(msg)

            self.data_socket.close()
            self.dataTochat_socket.close()
            return -1

        return 0

    def connecting_chat(self):
        try:
            self.dataTochat_socket.listen(1)
            (self.cs,sockname) = self.dataTochat_socket.accept()
        except socket.error msg:
            Log.error(msg)
            return -1

        return 0

    def run(self):
        while True:
            (data,address) = self.data_socket.recvfrom(MAX_SIZE_FROM_CLIENT)
            
