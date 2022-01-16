import socket
import json
import subprocess
from uuid import uuid4

serverSocket = socket.socket()
print("********Created the Socket!!********")

serverSocket.bind(("localhost", 9999))

serverSocket.listen()
print("********Waiting for Client to connect!!********")

while True:
    clientSocket, clientAddress = serverSocket.accept()

    print("Connected with Client at the address", clientAddress)

    jsonDumps = clientSocket.recv(1024).decode()
    print(jsonDumps)

    try:
        dataParse = json.loads(jsonDumps)

    except :
        print("Errorcode 1")
    command = (dataParse['command'])
    stdout = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    if len(command) > 0:
        print("Command to be Executed is:- ", command)


        result = subprocess.Popen(command, shell=True)

        if result.returncode == 0:

            output = ({ "stdout": stdout, "stderr": -1, "id": dataParse['id'], "Error code": " "})
            print(output)


        else:

            output = ({"stdout": stdout, "stderr": -1, "id": dataParse['id'], "Error code": 3})
            print(output)


    else:
        # print("Error code 2")

        output = ({"stdout": -1, "stderr": -1, "id": dataParse['id'], "Error code": 2})
        print(output)

        # print(result)

    # except subprocess.CalledProcessError as e:
    #     print("process Error")
    #
    # except OSError:
    #     print("OS Error")
    #
    # except Exception:
    #     print("I do not know !")



    clientSocket.send(bytes("*** Go check the Server for results !!***", "utf-8"))

