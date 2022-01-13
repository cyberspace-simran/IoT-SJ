import socket
import json
import subprocess



c=socket.socket()
c.connect(('localhost', 9999))


while True:
    name = input("Enter your name")
    c.send(bytes(name, 'utf-8'))

    cmd = input("Enter the os command")
    c.send(bytes(cmd, 'utf-8'))

    # data = {'command': cmd, 'id': '1'}
    # strData = json.dumps(data)
    # c.send((bytes(strData,'utf-8'))
    #tried it with json but was unsuccessful

client.close()