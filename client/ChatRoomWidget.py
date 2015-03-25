import sys
from PyQt4.Qt import *
from ChatClient import ChatOn
import ChatWidget

from client import asktoDM

import thread

class MyPopup(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		open_client()



class ChatRoomWidget(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setWindowTitle("Chating Room")
		self.create_main_frame()

	def create_main_frame(self):
		print 'Queries @ Chat Room'
		words = asktoDM()
		#2print words.queries

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
		print self.button[1]
		vbox1 = QVBoxLayout()
#2		vbox1.addWidget(self.button1)
#2		vbox1.addWidget(self.button2)

		print idx1
		for x in xrange(0, idx1):
			print 'x:', x
			vbox1.addWidget(self.button[x])

		page.setLayout(vbox1)
		self.setCentralWidget(page)

		for x in xrange(0, idx1):
			self.connect(self.button[x], SIGNAL("clicked()"), self.doit)		

#2		self.connect(self.button1, SIGNAL("clicked()"), self.doit)
#2		self.connect(self.button2, SIGNAL("clicked()"), self.doit)

	def doit(self):
		print "opening a new popup window"
		##self.w = MyPopup()
#3		#11self.w.setGeometry(Qrect(100, 100, 400, 200))
		##self.w.setGeometry(100, 100, 400, 200)
		##self.w.show()
		###thread.start_new_thread(open_client())
		self.chat = ChatOn(self)
		self.chat.show()

		#3self.wind = ChatWidget(self)
		#3self.wind.open_client()
		#4self.tkt = Example()
		#4main()

	def callChRoom(args, aaa):
		print aaa


"""
class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = MainWindow()
		self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye)
		self.main.show()

	def byebye(self):
		self.exit(0)
"""
"""
def main(args, aaa):
	print aaa
	global app
	app = App(args)
	app.exec_()
"""

if __name__ == "__main__":
	chatroom = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(chatroom.exec_())
	main(sys.argv)
