import socket
import sys
import const
from _thread import *
from http.server import BaseHTTPRequestHandler, HTTPServer

PRIVATE_HOST_SERVER = const.SERVER_ADDR
PUBLIC_HOST_CLIENT1 = const.CLIENT1_ADDR
PORT = const.PORT

socket = socket.socket()

print('Server running on port: ', PORT)

class HandlerConnection(BaseHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		req_data = self.rfile.read(content_length)
		print(req_data)

try:
	server = HTTPServer((PRIVATE_HOST_SERVER, PORT), HandlerConnection)
	print('Starting server...')
	server.serve_forever()
except Exception as error:
	print('Server error')
	print('Error')
