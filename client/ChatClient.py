#! /usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

PORTS = (9998, 9999)
PORT = 9999
SIZEOF_UINT32 = 4

class ChatOn(QDialog):

	def __init__(self, parent=None, groupId=None):
		super(ChatOn, self).__init__(parent)

		self.groupID = groupId
		###print 'groupID+++: ',groupId, ' / ', self.groupID

		# Ititialize socket
		self.socket = QTcpSocket()

		# Initialize data IO variables
		self.nextBlockSize = 0
		self.request = None
		self.firstTime = True

		# Create widgets/layout
		self.browser = QTextBrowser()
		self.lineedit = QLineEdit("Enter text here, dummy")
		self.lineedit.selectAll()
		self.connectButton = QPushButton("Connect")
		self.connectButton.setEnabled(True)
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		layout.addWidget(self.connectButton)
		self.setLayout(layout)
		self.lineedit.setFocus()

		# Signals and slots for line edit and connect button
		self.lineedit.returnPressed.connect(self.issueRequest)
		self.connectButton.clicked.connect(self.connectToServer)

		self.setWindowTitle("Client")
		# Signals and slots for networking
		self.socket.readyRead.connect(self.readFromServer)
		self.socket.disconnected.connect(self.serverHasStopped)
		self.connect(self.socket,
					 SIGNAL("error(QAbstractSocket::SocketError)"),
					 self.serverHasError)

	# Update GUI
	def updateUi(self, text):
		self.browser.append(text)

	# Create connection to server
	def connectToServer(self):
		self.connectButton.setEnabled(False)
		self.socket.connectToHost('localhost', PORT)
		print 'Local IP port', self.socket.localAddress().toString(), '/', self.socket.localPort()

	def issueRequest(self):
		self.request = QByteArray()
		stream = QDataStream(self.request, QIODevice.WriteOnly)
		stream.setVersion(QDataStream.Qt_4_2)
		stream.writeUInt32(0)
		if self.firstTime:
			stream << QString("AUTH") << QString(self.lineedit.text()) << QString(str(self.groupID))
			self.firstTime = False
		else:
#org			stream << QString("SEND") << QString(self.lineedit.text())
			stream << QString("SEND") << QString(self.lineedit.text()) << QString(str(self.groupID))
		stream.device().seek(0)
		stream.writeUInt32(self.request.size() - SIZEOF_UINT32)
		self.socket.write(self.request)
		self.nextBlockSize = 0
		self.request = None
		self.lineedit.setText("")

	def readFromServer(self):
		stream = QDataStream(self.socket)
		stream.setVersion(QDataStream.Qt_4_2)

		while True:
			if self.nextBlockSize == 0:
				if self.socket.bytesAvailable() < SIZEOF_UINT32:
					break
				self.nextBlockSize = stream.readUInt32()
			if self.socket.bytesAvailable() < self.nextBlockSize:
				break
			action = QString()
			textFromServer = QString()
			stream >> action >> textFromServer
			if action == "CHAT":
				self.updateUi(textFromServer)
			elif action =="AUTH":
				self.updateUi(textFromServer)
				self.firstTime = True
			self.nextBlockSize = 0

	def serverHasStopped(self):
		self.socket.close()
		self.connectButton.setEnabled(True)

	def serverHasError(self):
		self.updateUi("Error: {}".format(
				self.socket.errorString()))
		self.socket.close()
		self.connectButton.setEnabled(True)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = ChatOn()
	form.show()
	app.exec_()
