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
		#!print 'Queries @ Chat Room: ',self.username
		words = asktoDM(self.username)
#11		print 'words'
#11		print words

		page = QWidget()

		if words == []:	# case that there is no groups
			self.button = QPushButton('Quit', page)
			self.label = QLabel('No Chat Group', page)
			self.connect(self.button, SIGNAL("clicked()"),self.close)

			vbox1 = QVBoxLayout()
			vbox1.addWidget(self.label)
			vbox1.addWidget(self.button)

			page.setLayout(vbox1)
			self.setCentralWidget(page)
		else:
			idx1 = 0
			self.button = []
			for wl in words:
				print wl
				if idx1 == 2:
					break
				self.button.append( QPushButton(','.join(wl.data), page) )
				idx1 = idx1 + 1

			vbox1 = QVBoxLayout()

			for x in xrange(0, idx1):
				vbox1.addWidget(self.button[x])

			page.setLayout(vbox1)
			self.setCentralWidget(page)

			for x in xrange(0, idx1):
				#!self.connect(self.button[x], SIGNAL("clicked()"), lambda: self.doit(words[x].ID))
				self.connect(self.button[x], SIGNAL("clicked()"), partial(self.doit, words[x].ID))


	def doit(self, tstr):
		#!print "opening a new popup window ", tstr
		self.chat = ChatOn(self, tstr)
		self.chat.show()


if __name__ == "__main__":
	chatroom = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(chatroom.exec_())
	main(sys.argv)
