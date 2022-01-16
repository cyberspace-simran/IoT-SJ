import socket
import json
import subprocess
from uuid import uuid4

"""
here we are creating the socket and connecting it to localhost on port 9999 since 
we are making the connection of server and client on the same system.
"""
serverSocket = socket.socket()
print("********Created the Socket!!********")

"""
 Next we bind to the port 
 make the server listen to the client
"""
serverSocket.bind(("localhost", 9999))

# put the socket into listening mode

serverSocket.listen()
print("********Waiting for Client to connect!!********")

while True:
    """
    Establishing connection with client.
    """
    clientSocket, clientAddress = serverSocket.accept()

    print("Connected with Client at the address", clientAddress)

    """
    
    receive json from the client and decoding to get the string.
    """

    jsonDumps = clientSocket.recv(1024).decode()
    print(jsonDumps)

    """
     trying to check for exceptions.
     """

    try:
        dataParse = json.loads(jsonDumps)

    except :
        print("Errorcode 1")
    command = (dataParse['command'])
    stdout = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    """
    if there is no command given the code should throw invalid request error
    """

    if len(command) > 0:
        print("Command to be Executed is:- ", command)


        result = subprocess.run(command, shell=True)

        if result.returncode == 0:

            output = ({ "stdout": stdout, "stderr": stdout.stderr, "id": dataParse['id'], "Error code": "None"})
            print(output)


        else:

            output = ({"stdout": stdout, "stderr": stdout.stderr, "id": dataParse['id'], "Error code": 3})
            print(output)


    else:
        # print("Error code 2")

        output = ({"stdout": -1, "stderr": stdout.stderr, "id": dataParse['id'], "Error code": 2})
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

    serverSocket.close()