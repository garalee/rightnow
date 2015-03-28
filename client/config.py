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

    LOG_FILE_PATH_CHAT = 'log/rightnow_chat.log'
    LOG_FILE_PATH_DATA = 'log/rightnow_data.log'
    LOGGER_NAME_CHAT = 'rightnowlogger_chat'
    LOGGER_NAME_DATA = 'rightnowlogger_data'
