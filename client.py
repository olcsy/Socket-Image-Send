# -*- coding: cp1254 -*-
import time
import sys
import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "HOST-NAME"
port = 8080


s.connect((host,port))
print("")
print("Connected to server")




while True:
    filename='Lighthouse.jpg'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       s.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    s.close()
