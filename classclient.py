import socket
import json
from uuid import uuid4
import subprocess

class Client:
    """
    creating a class of the client
    """
    def __init__(self):
        """
        Create a socket object for the client side
        """
        self.clientSocket = socket.socket()
        """
        # connect to the server on local computer
        """
        self.clientSocket.connect(('localhost', 9999))

    def send(self):
        """
        # send json data to the server
        """
        cmd = input("Enter your os command")
        dataF = {'command': cmd, 'id': str(uuid4())}
        jsonDumps = json.dumps(dataF)
        print(jsonDumps)

        self.clientSocket.send(bytes(jsonDumps, 'utf-8'))
        # print(finalResult)
    def receive(self):
        """
        receive data from the server and decoding to get the string.
        """
        print(self.clientSocket.recv(1024).decode())


clientCreated = Client()
clientCreated.send()
clientCreated.receive()





