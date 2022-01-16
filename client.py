"""
importing the required modules
"""

import socket
import json
from uuid import uuid4
import subprocess

"""
Create a socket object for the client side
"""

clientSocket = socket.socket()
"""
# connect to the server on local computer
"""
clientSocket.connect(('localhost', 9999))

"""
# send json data to the server 
"""
cmd = input("Enter your os command")
dataF = {'command': cmd, 'id': str(uuid4())}
jsonDumps= json.dumps(dataF)
print(jsonDumps)

clientSocket.send(bytes(jsonDumps,'utf-8'))
# print(finalResult)
"""
receive data from the server and decoding to get the string.
"""
print(clientSocket.recv(1024).decode())
