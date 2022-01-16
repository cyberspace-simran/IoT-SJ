import socket
import json
from uuid import uuid4
import subprocess

clientSocket = socket.socket()

clientSocket.connect(('localhost', 9999))


cmd = input("Enter your os command")
dataF = {'command': cmd, 'id': str(uuid4())}
jsonDumps= json.dumps(dataF)
print(jsonDumps)

clientSocket.send(bytes(jsonDumps,'utf-8'))
# print(finalResult)
print(clientSocket.recv(1024).decode())
