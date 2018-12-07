import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 90
MESSAGE = b"Hello, World!"

if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
	print (data)		
	time.sleep(1)	