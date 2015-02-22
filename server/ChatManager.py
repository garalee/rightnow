import socket

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
            self.chatTodata_socket.connect((RightnowConfig.DATA_TO_CHAT_IP,DATA_TO_CHAT_PORT))
        except socket.error, msg:
            Log.error(msg)

            self.chatTodata_socket.close()
            self.chat_socket.close()
            return -1

        return 0

    def run(self):
        pass
