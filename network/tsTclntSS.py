#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 22677
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(('{}'.format(data)).encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()
