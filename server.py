import socket
import json
import subprocess
from uuid import uuid4


s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen()
print('waiting for connection')
c, addr = s.accept()
print("connected")
while True:

    # name = c.recv(1024).decode()

    cmd = c.recv(1024).decode()
    subprocess.Popen(cmd, shell=True)
    strData = c.recv(1024).decode()

    print("connected with",addr)
    print(strData)

    # print("NEW CONNECTION:", addr)
    c.send(strData.encode("utf-8"))

    clientResponse = c.recv(2048).decode("utf-8")
    print("Client response:", clientResponse)


    c.send(bytes("We are connected", "utf -8 "))

connection.close()