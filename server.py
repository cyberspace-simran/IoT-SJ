import socket
import json
import subprocess

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen()
print('waiting for connection')
c, addr = s.accept()
print("connected")
while True:

    name = c.recv(1024).decode()
    cmd = c.recv(1024).decode()
    subprocess.Popen(cmd, shell=True)

    # data = {'command': cmd, 'id': '1'}
    # strData = json.dumps(data)
    # strData = c.recv(1024).decode()

    print("connected with",addr,"name", name,"command", cmd)


    c.send(bytes("We are connected", "utf -8 "))

connection.close()