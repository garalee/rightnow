import time
import os

from config import RightnowConfig
import threading
import DataManager
import ChatManager

logger_name = RightnowConfig.LOGGER_NAME_DATA
log_filepath = RightnowConfig.LOG_FILE_PATH_DATA
from rightnow_logger import Log
Log.init(logger_name = logger_name,log_filepath=log_filepath)


class DM(threading.Thread):
    def __init__(self):
        self.d = DataManager.DataManager()
        
    def run(self):
        if self.d.socket_init() == -1:
            Log.error("Program Exited")
            exit(-1)

        Log.info("Data Socket Initialized")
        #1Log.info("Wait For Chatting Manager...")
        #1if self.d.connecting_chat() == 0: Log.info("DataToChat Socket Connected")
        #1else: exit(-1)

        self.d.run()


class CM(threading.Thread):
    def __init__(self):
        self.c = ChatManager.ChatManager()

    def run(self):
        if self.c.socket_init() == -1:
            Log.info("Program Exited")
            exit(-1)

        Log.info("Chat Socket Initialized")
        Log.info("Connecting To Data Manager")
        if self.c.connecting_data() == 0:Log.info("ChatToData Socket Connected")
        else:exit(-1)

        self.c.run()
