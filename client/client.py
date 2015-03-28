from model import DataPacket

import socket
import threading
import pickle

#--from run import setGroupID

from config import RightnowConfig


clisockfd = 0
is_first = 1
received_msg = []
ds_port = RightnowConfig.DATA_SERVER_PORT
ds_ip = RightnowConfig.DATA_SERVER_IP

def receiver():
	while 1:
		rmsg = clisockfd.recv(100)
		print rmsg
		received_msg = rmsg.split(',')
		print received_msg#--[0]
		#--setGroupID( received_msg[1] )

def sendtosvr(clisock, datagram):
	global clisockfd
	clisockfd = clisock

	global is_first
	#clisock.connect( ('', 23000) )
	#clisock.connect( ('', RightnowConfig.DATA_SERVER_PORT) )
	#22clisock.connect( ('localhost', 12356) )

	#22clisock.send(datagram)

	received = datagram.split(',')
	print received[len(received)-1:len(received)],' ',received[0:len(received)-1]
	#1dp = DataPacket.DataPacket( '', received[0:len(received)-1], '', received[len(received)-1:len(received)], 0 )
	dp = DataPacket.DataPacket( received[len(received)-1:len(received)], 0, received[0:len(received)-1] ) # ID, flag, data
	#22clisock.sendto(datagram, ('localhost', 12356))
	clisock.sendto( pickle.dumps(dp), (ds_ip, ds_port) )


	print 'sent...'

	if is_first == 1:
		t = threading.Thread(target=receiver)
		t.start()

	is_first = 0

#	clisock.close()

def asktoDM(username):
	clientsock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
	dp = DataPacket.DataPacket( [username], 2, '' )
	clientsock.sendto( pickle.dumps(dp), (ds_ip, ds_port) )

	print 'asked...'

	(data,address) = clientsock.recvfrom(1024)
	#2words = pickle.loads ( data )
	wordslist = pickle.loads ( data )
	#2print words.queries
	#2return words
	return wordslist

