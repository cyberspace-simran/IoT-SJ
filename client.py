import socket
import json
import subprocess
import os
from uuid import uuid4

c = socket.socket()
c.connect(('localhost', 9999))

while True:
    # name = input("Enter your name")
    # c.send(bytes(name, 'utf-8'))

    cmd = input("Enter the os command")
    data = {'command': cmd, 'id': str(uuid4())}

    c.send(bytes(cmd, 'utf-8'))
    strData = json.dumps(data)
    c.send(bytes(strData, 'utf-8'))

    cmd = c.recv(2048).decode("utf-8")
    errcode = -1

    try:
        # data = json.loads(cmd)
        strData = json.dumps(data)

    except:
        errcode = 1

    if errcode == -1:
        print("command is:", data['command'])

        result = ""
        stdout = ""
        try:
            result = os.system(data["command"])
            stdout = subprocess.run(data["command"], stdout=subprocess.PIPE).stdout.decode('utf-8')
            print("standard output:", stdout)
        except:
            errcode = 3

        id = data["id"]
        to_send = {"result": result, "stdout": stdout, "errcode": errcode, "id": id}
        str_to_send = json.dumps(to_send)
        c.send(str_to_send.encode("utf-8"))

c.close()
