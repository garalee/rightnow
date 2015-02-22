class RightnowConfig(object):
    
    CHAT_SERVER_IP = 'localhost'
    DATA_SERVER_IP = 'localhost'

    CHAT_SERVER_PORT = 12314
    DATA_SERVER_PORT = 12356

    DATA_TO_CHAT_IP = 'localhost'
    CHAT_TO_DATA_IP = 'localhost'

    DATA_TO_CHAT_PORT = 12435
    CHAT_TO_DATA_PORT = 12436

    MAX_SIZE_FROM_CLIENT = 1024

    LOG_FILE_PATH = 'log/rightnow.log'
    LOGGER_NAME = 'rightnowlogger'
