#!/usr/bin/env python3

import socket
from time import ctime

HOST = ''
PORT = 22335
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpss.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpss.recvfrom(BUFSIZ)
    udpss.sendto(('[{0}] {1}'.format(ctime(), data)).encode('utf-8'), addr)
    print('received from and return to: ',addr)

    
