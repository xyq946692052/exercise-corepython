#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 22335
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpcli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpcli.sendto(data.encode('utf-8'), ADDR)
    data, addr = udpcli.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode())    
