# -*- coding: utf-8

import threading,socket
import Queue
from PyQt4 import QtCore,QtGui

class ChatClient(QtGui.QWidget):
    HOST = '127.0.0.1'
    SEND_PORT = 9876
    RECV_PORT = 9875

    def __init__(self,username,parent=None):
        super(ChatClient,self).__init__(parent)

        self.resize(300,500)
        self.queue = Queue.Queue()
        self.username = username
        self.chatVerticalLayout = QtGui.QVBoxLayout(self)

        self.chat_screen = QtGui.QTextEdit()
        self.chat_input = QtGui.QLineEdit()
        self.chat_screen.setReadOnly(True)
        self.chatVerticalLayout.addWidget(self.chat_screen)
        self.chatVerticalLayout.addWidget(self.chat_input)

        QtCore.QObject.connect(self.chat_input,QtCore.SIGNAL("returnPressed()"), self.sendMessage)
        QtCore.QObject.connect(self.chat_screen,QtCore.SIGNAL("chatRequested(const QString&,const QString&)"),self.recvMessage)
                               
        self.setWindowTitle('Chatting')
        self.hide()

        self.socket_init()

    def socket_init(self):
        # socket setting
        self.send_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.recv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.send_socket.connect((ChatClient.HOST,ChatClient.SEND_PORT))
        self.recv_socket.connect((ChatClient.HOST,ChatClient.RECV_PORT))

        self.send_socket.send(self.username)
        self.recv_thread = threading.Thread(target=self.recv_thread).start()

        
    def recv_thread(self):
        while True:
            try:
                username = self.recv_socket.recv(1024)
                msg = self.recv_socket.recv(1024)

                if not msg:
                    print "RECV THREAD HAS STOPPED"
                    break
                
                self.chat_screen.emit(QtCore.SIGNAL("chatRequested(const QString&,const QString&)"),username,msg)

            except:
                print "socket error"
                break

        print "RECV THREAD DONE.."

    def send_message(self,msg):
        self.send_socket.send(msg)

    def recv_message(self):
        if not self.queue.empty():
            self.lock.acquire()
            msg = self.queue.get()
            self.lock.release()
        
            self.chat_screen.append(msg)


    def sendMessage(self):
        t = self.chat_input.text()
        if t:
            self.chat_input.clear()
            self.send_message(str(t))

    def recvMessage(self,username,msg):
        # self.chatClient.recv_message()
        print "user name is ", username
        print "message is ", msg
        try:
            if username == self.username:
                self.chat_screen.insertHtml("<div style='color:red'>" + username + " : " + msg + "<br/></div>")
            else:
                self.chat_screen.insertHtml("<div>" + username + " : " + msg + "<br/></div>")
        except:
            print "Exception"
		