import sys
from PyQt4.Qt import *
from ChatClient import ChatOn

from client import asktoDM
from functools import partial

import thread


class ChatRoomWidget(QMainWindow):
	userId = None

	def __init__(self, parent=None, username=None):
		QMainWindow.__init__(self, parent)
		self.username = username
		self.setWindowTitle("Chating Room")
		self.create_main_frame()

	def create_main_frame(self):
		print 'Queries @ Chat Room: ',self.username
		words = asktoDM(self.username)
		print words

		page = QWidget()
#		self.button1 = QPushButton('keyword 1', page)
#2		self.button1 = QPushButton(words.queries[0], page)
#		self.button2 = QPushButton('keyword 2', page)
#2		self.button2 = QPushButton(','.join(words.queries), page)

		idx1 = 0
		self.button = []
		for wl in words:
			if idx1 == 2:
				break
			self.button.append( QPushButton(','.join(wl.data), page) )
			idx1 = idx1 + 1


		print 'len:', len(self.button)
		print self.button[0]
		vbox1 = QVBoxLayout()
#2		vbox1.addWidget(self.button1)
#2		vbox1.addWidget(self.button2)

		print idx1
		for x in xrange(0, idx1):
			vbox1.addWidget(self.button[x])

		page.setLayout(vbox1)
		self.setCentralWidget(page)

		for x in xrange(0, idx1):
			print 'x:', x, ' / ',words[x].ID
###			self.connect(self.button[x], SIGNAL("clicked()"), lambda: self.doit(words[x].ID))
			self.connect(self.button[x], SIGNAL("clicked()"), partial(self.doit, words[x].ID))

#2		self.connect(self.button1, SIGNAL("clicked()"), self.doit)
#2		self.connect(self.button2, SIGNAL("clicked()"), self.doit)

	def doit(self, tstr):
		print "opening a new popup window ", tstr
		self.chat = ChatOn(self, tstr)
		self.chat.show()


if __name__ == "__main__":
	chatroom = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(chatroom.exec_())
	main(sys.argv)
