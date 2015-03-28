# -*- coding: utf-8 -*-
import sys
import threading
import socket
#######from chat import ChatClient
from PyQt4 import QtCore, QtGui
from httpWidget import Ui_HttpWidget
import urllib
from urlparse import parse_qsl

from Util import returnRId

#1. from pyfb import Pyfb

from time import gmtime,strftime

#from alchemy import parsing
from client import sendtosvr
#######from ChatClient import chat_client
from ChatRoomWidget import ChatRoomWidget

import csv

is_first = 0
#1. email_id = 'abc@facebook.com'#'Default'
email_id = None
clisock = 0
groupID = 0

def setGroupID( gid ):
	global groupID
	groupID = gid

	print 'groupID: ', groupID

class httpWidget(QtGui.QWidget):
	global is_first
	is_first = 0

	global clisock
	#22clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	clisock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

	def __init__(self,parent=None):
		super(httpWidget, self).__init__(parent)
		self.ui = Ui_HttpWidget()
		self.ui.setupUi(self)

		self.fp = open("dataset.csv",'a')
		self.writer = csv.writer(self.fp,delimiter=',')
		#self.chatClient = ChatClient(username)
		# set margins
		l = self.layout()
		l.setMargin(0)
		self.ui.horizontalLayout.setMargin(5)

		#############################################################################
		#Part for FACEBOOK Authentication											#
		# remove '#1. ' when FACEBOOK login is needed								#
		#############################################################################

		#1. FACEBOOK_APP_ID = '178358228892649'
		#1. self.facebook = Pyfb(FACEBOOK_APP_ID)
		#############################################################################
		##>facebook.authenticate()													#
		#############################################################################
		#1. self.facebook.set_permissions(["user_about_me", "email"])
		#1. url = urllib.unquote( self.facebook.get_auth_url() )

		# set the default
		##>url = 'http://localhost:8080'
		##>url = 'https://www.facebook.com/dialog/oauth?scope=user_about_me&redirect_uri=http://www.facebook.com/connect/login_success.html&type=user_agent&client_id=178358228892649'
		url = 'http://www.google.com/'	# comment when FACEBOOK login is needed
		self.ui.url.setText(url)

		# load page
		self.ui.webView.setUrl(QtCore.QUrl(url))
		# history buttons:
		self.ui.back.setEnabled(False)
		self.ui.next.setEnabled(False)

		QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
		QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL("clicked()"), self.next)
		QtCore.QObject.connect(self.ui.url,QtCore.SIGNAL("returnPressed()"), self.url_changed)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadFinished(bool)"),self.urlExtract)
		QtCore.QObject.connect(self.ui.reload,QtCore.SIGNAL("clicked()"), self.reload_page)
		QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_page)

		QtCore.QObject.connect(self.ui.chat,QtCore.SIGNAL("clicked()"), self.chatClicked)
	
		QtCore.QMetaObject.connectSlotsByName(self)
	

	def urlExtract(self):
		global is_first, email_id

		url = self.ui.url.text()

		if "?" in url:
			dataset = url.split("?")[1]
			for data in dataset.split("&"):
				key = data.split("=")[0]
				value = data.split("=")[1]

				if key == "q":
					record = [str(v) for v in value.split("+")]
					time_record = strftime("%Y-%m-%d %H:%M:%S", gmtime())
					record.append(time_record)
					self.writer.writerows([record])

		if "#" in url:
			dataset = url.split("#")[1]
			for data in dataset.split("&"):
				key = data.split("=")[0]
				value = data.split("=")[1]

				#1. if key == "access_token":
				#1. 	access_token = value
				#1. 	self.facebook.set_access_token(access_token)
				#1. 	self.facebook.set_permissions("email")
				#1. 	me = self.facebook.get_myself()
				#1. 	print "-" * 40
				#1. 	print "ID\t: %s" % me.id
				#1. 	print "E-mail\t: %s" % me.email
				#1. 	email_id = me.email
				#1. 	print "Name\t: %s" % me.name
				#1. 	print "From\t: %s" % me.hometown.name
				#1. 	print

					#print "Speaks:"
					#for language in me.language:
					#    print "- %s" % language.name

				#1. 	print
				#1. 	print "Worked at:"
				#1. 	for work in me.work:
				#1. 		print "- %s" % work.employer.name

				#1. 	print "-" * 40
				#1. 	self.ui.webView.setUrl(QtCore.QUrl("http://www.google.com/"))
					###is_first = 1

		## ??? added part
#		print "url: ", url

#		page1 = self.ui.webView.page()
#		frame = page1.currentFrame()
#		content = frame.toHtml()

#		print unicode( content ).encode('utf-8')
		#parsing( unicode( content ).encode('utf-8') )

		# From 2nd url extraction(is_first == 1), queries should be sent to DataManager in Server
		if is_first == 1:
			if "?" in url:
				dataset = url.split("?")[1]
				for data in dataset.split("&"):
					key = data.split("=")[0]
					value = data.split("=")[1]

					if key == "q":
						record = [str(v) for v in value.split("+")]
						record.append( email_id )
#2						print record
						sendtosvr(clisock, ','.join(record))
#1			parsing( url )
		else:
			# If system needs to keep Facebook email id as a username, then send a flag telling Facebook ID or temp ID.
			# So, let Data Server not delete Facebook ID based on the flag even it is expired. 
			if email_id == None :
				email_id = returnRId()

		print 'email_id: ', email_id
		is_first = 1
		## ??? added part


	def chatClicked(self):
		"""
		if self.chatClient.isHidden():
			self.chatClient.show()
		else:
			self.chatClient.hide()
		"""
		#--chat_client( 'localhost', 2626)
		#11main(sys.argv, 'adf')
		global email_id
		self.chroom = ChatRoomWidget(self, email_id)
		self.chroom.show()


	def url_changed(self):
		"""
		Url have been changed by user
		"""

		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		url = self.ui.url.text()

		if (not ("http://" in url)) or (not ("https://")):
			url = "http://" + url
			
		self.ui.webView.setUrl(QtCore.QUrl(url))

	def stop_page(self):
		"""
		Stop loading the page
		"""
		self.ui.webView.stop()
	
	def title_changed(self, title):
		"""
		Web page title changed - change the tab name
		"""
		self.setWindowTitle(title)
	
	def reload_page(self):
		"""
		Reload the web page
		"""
		self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))

	
	
	def link_clicked(self, url):
		"""
		Update the URL if a link on a web page is clicked
		"""
		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)

		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		self.ui.url.setText(url.toString())

		## ??? added part
		#print "TEST: ", url.toString()
		## ??? added part

	
	def load_progress(self, load):
		"""
		Page load progress
		"""
		if load == 100:
			self.ui.stop.setEnabled(False)
		else:
			self.ui.stop.setEnabled(True)
		
	def back(self):
		"""
		Back button clicked, go one page back
		"""
		page = self.ui.webView.page()
		history = page.history()
		history.back()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
	
	def next(self):
		"""
		Next button clicked, go to next page
		"""
		page = self.ui.webView.page()
		history = page.history()
		history.forward()
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)

	def closeEvent(self,e):
		self.fp.close()


	def keyPressEvent(self,e):
		if ((e.key() == QtCore.Qt.Key_L) and (QtGui.QApplication.keyboardModifiers() & QtCore.Qt.ControlModifier)):
			self.ui.url.selectAll()
			self.ui.url.setFocus()



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = httpWidget()
	myapp.show()
	sys.exit(app.exec_())
