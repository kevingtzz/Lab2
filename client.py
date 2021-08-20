import socket
import sys
import ipaddress
import requests
import http.client
import const

PRIVATE_HOST_SERVER = const.SERVER_ADDR
PUBLIC_HOST_SERVER_PORT = const.PUBLIC_SERVER_ADDR_PORT
PORT = const.PORT

socket = socket.socket()

try:
	while(True):
		message = input('Enter a message:')
		req = requests.post(PUBLIC_HOST_SERVER_PORT, message)
		print(req)

except (IndexError, ValueError):
	print('Error')
