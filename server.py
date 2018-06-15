#!/usr/bin/env python

import socket


TCP_IP = '10.10.124.243'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen()
count=0
while 1:
	conn, addr = s.accept()
	print ('Connection address:', addr)
	while 1:
		data = conn.recv(BUFFER_SIZE)
		if not data: break
		print ("received data:", data)
		conn.send('Done'.encode())  # echo
		count = count+1
	conn.close()
	print('Connection closed', '\n')
	
	if count ==4: break
	