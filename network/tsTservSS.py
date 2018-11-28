#!/usr/bin/env pyhton3

from socketserver import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 22676
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from: ', self.client_address)
        self.wfile.write(('[{0}] {1}'.format(ctime(), self.rfile.readline())).encode('utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()


