import time
import sys
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
print(host)

port = 8080
s.bind((host,port))

print("")
print("Bağlantı için bekleniliyor..")
print("")

s.listen(1)
conn,addr = s.accept()

print("")
print(addr,"- Has Connected to the server")
print("")


with open('received_file.jpg', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = conn.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

