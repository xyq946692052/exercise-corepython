#!/usr/bin/env python3

import socket
from time import ctime

HOST = ''
PORT = 22356
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpss.bind(ADDR)
tcpss.listen(5)

while True:
    try:
        print('waiting for connection...')
        ncli, addr = tcpss.accept()
        print('...connection from ', addr)
    
        while True:
            data = ncli.recv(BUFSIZ)
            if not data:
                break
            ncli.send(('{}-from service: {}'.format(ctime(), data)).encode('utf-8'))
        ncli.close()
    except:
        tcpss.close()
