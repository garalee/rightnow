import socket
from rightnow_logger import Log
from config import RightnowConfig

class DataManager:
    def socket_init(self):
        try:
            self.data_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.dataTochat_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            self.data_socket.bind((RightnowConfig.DATA_SERVER_IP,RightnowConfig.DATA_SERVER_PORT))
            self.dataTochat_socket.bind((RightnowConfig.DATA_TO_CHAT_IP,RightnowConfig.DATA_TO_CHAT_PORT))

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
        except socket.error,msg:
            Log.error(msg)
            return -1
        return 0

    def run(self):
        while True:
            (data,address) = self.data_socket.recvfrom(MAX_SIZE_FROM_CLIENT)
            
if __name__ == "__main__":
    d = DataManager()

    # Setting Logger
    logger_name = RightnowConfig.LOGGER_NAME_CHAT
    log_filepath = RightnowConfig.LOG_FILE_PATH_CHAT
    from rightnow_logger import Log
    Log.init(logger_name = logger_name,log_filepath=log_filepath)

    Log.info("Starting Server...")
    if d.socket_init() == -1:
        Log.error("Socket Init Failed : Program Exited")
        exit(-1)

    Log.info("Data Socket Initialized")
    Log.info("Wait For Chatting Manager...")
    if d.connecting_chat() == 0:
        Log.debug("DataToChat Socket Connected")

    d.run()
