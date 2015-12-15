import socket, sys, time

EOF = '\n'
DOWNLOAD_OPCODE = 'DOWNLOAD'

def test_upload(host, port, payloadsize):
	payload = "v"*payloadsize + EOF
	payload_bytes = bytearray(payload, 'ascii')
	#							IP4 			TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	print("connected to server at "+host+":"+str(port))
	sent = 0
	size = len(payload_bytes)
	print("payload contains "+str(size-len(EOF))+" bytes. beginning transfer")
	starttime = time.time()
	while sent < size:
		# start sending where you left off; ie send_base
		# inc is the number of bytes sent
		inc = s.send(payload_bytes[sent:])
		if inc == 0:
			# done
			break #nop
		sent += inc
	elapsed = time.time() - starttime
	print("done sending file. it took " + str(elapsed) + " seconds!")
	# server supposed to send back the number of bytes rec'd
	bytes_recd = s.recv(1024)
	print("successfully sent "+bytes_recd.decode('ascii')+" bytes to "+host)
	#s.shutdown(socket.SHUT_RDWR)
	s.close()
	print("successfully shut down socket")	
	return elapsed

def test_download(host, port, payloadsize):
	payload = DOWNLOAD_OPCODE + " " + str(payloadsize)
	payload_bytes = bytearray(payload, 'ascii')
	#							IP4 			TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	print("connected to server at "+host+":"+str(port)+" for dowload testing...")
	sent = 0
	size = len(payload_bytes)
	print("payload contains "+str(size-len(EOF))+" bytes. beginning transfer")
	inc = s.send(payload_bytes[sent:])
	if inc == 0:
		print("houston, we have a problem. failed to send request to server")
	# now we've told the server how many bytes we want back, so receive them
	starttime = time.time()
	numbytes = readfile(s)
	elapsed = time.time() - starttime


def readfile(s):
	last_rcvd = bytearray()
	numbytes = 0
	# receive until we hit the delimiter
	while EOF not in last_rcvd.decode('ascii'):
		last_rcvd = s.recv(1024)
		numbytes += len(last_rcvd)
		if DOWNLOAD_OPCODE in last_rcvd.decode('ascii'):
			# tell the caller that they should take some other action
			# message format = "DOWNLOAD <numbytes>"
			message = last_rcvd.decode('ascii')
			print("ooh, we should send back "+message[len(DOWNLOAD_OPCODE+1)]+" bytes")
			return -1 * eval(message[len(DOWNLOAD_OPCODE+1)])
	print('done receiving data')
	return numbytes

def sendfile(s, size):
	pass

def server(portnum):
	#							IP4 			TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	hostname = socket.gethostname()
	if hostname == ' ':
		# invalid hostname
		hostname = 'testhost'
	# bind to 0.0.0.0 to accept connections from anywhere
	s.bind(('0.0.0.0', portnum))
	print("listening for data coming in on port "+str(portnum))
	s.listen(1)
	while True:
		# loop in here, accepting data forever
		# get a connection!!!
		(client_s, addr) = s.accept()
		print("successfully connected to client "+str(addr))
		bytes_recd = readfile(client_s)
		if bytes_recd < 0:
			sendfile(s, -1 * bytes_recd)

			payload = "v"*length_reqd + EOF
			continue
		print("transfer complete! received "+str(bytes_recd - len(EOF))+" bytes")
		client_s.send(str(bytes_recd - len(EOF)))
		print("sent file transfer confirmation message to client")
	
	print("closing socket...")
	s.shutdown(socket.SHUT_RDWR)
	s.close()
	return 1

if __name__ == '__main__':
	# then it's being run as a command-line server
	# not being called from the gui
	#test_upload("test.mattpiazza.com", 8080, eval(sys.argv[1]))
	#try:
	#	server(eval(sys.argv[1]))
	#except KeyboardInterrupt:
	#	print("good testing, see you soon")