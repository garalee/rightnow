import time
import os

from config import RightnowConfig
import threading
import server



if __name__ == "__main__":
    dataManager = server.DM()
    chatManager = server.CM()

    dataManager.run()
    time.sleep(3)
    chatManager.run()
