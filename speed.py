import socket, sys

EOF = '\n'

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
	while sent < size:
		# start sending where you left off; ie send_base
		# inc is the number of bytes sent
		inc = s.send(payload_bytes[sent:])
		if inc == 0:
			# done
			break #nop
		sent += inc
	print("done sending file")
	# server supposed to send back the number of bytes rec'd
	bytes_recd = s.recv(1024)
	print("successfully sent "+bytes_recd.decode('ascii')+" bytes to "+host)
	#s.shutdown(socket.SHUT_RDWR)
	s.close()
	print("successfully shut down socket")	
	return

if __name__ == '__main__':
	#main()
	#test_upload("mattpiazza.com", 8080, 15)