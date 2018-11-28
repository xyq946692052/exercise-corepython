#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 22356
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpcli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpcli.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpcli.send(data.encode('utf-8'))
    data = tcpcli.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcpcli.close()
