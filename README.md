# IoT-SJ

Here there are 2 pair of files:
1. <a href = "https://github.com/cyberspace-simran/IoT-SJ/blob/main/server.py" target="_blank">Server.py<a/> and <a href = "https://github.com/cyberspace-simran/IoT-SJ/blob/main/client.py" target="_blank"> Client.py</a> 
 In this pair I have implemented the below task without any class implemantation

 2. <a href= https://github.com/cyberspace-simran/IoT-SJ/blob/main/classserver.py>ClassServer.py</a> and <a href ="https://github.com/cyberspace-simran/IoT-SJ/blob/main/classclient.py">ClassClient.py</a>  
  In this pair I have tried implementing the below task with in an **object oriented** manner i.e classes. 
    
    
## **Task**

Implement a communication channel between raw socket client and raw socket server using socket programming in python such that the client is able to execute any OS command on the server.

**Client side**

- Sends the request JSON object to the server.
- The request JSON object has the following members :
    - method : any linux OS command (This OS command will be executed by the server in its environment)
        - Some examples can be mkdir, rm, touch, date, uptime, hostname, ping etc.
    - id : An unique identifier that must contain a unique number. The server must reply with the same id in the response object.

**Server side**

- Receives the request JSON object sent from the client.
- Parses the JSON object and executes the os command as included in the request object using the python standard subprocess library.
- Replies to the client with a response. The response is a single JSON object with the following members :
    - result : return code of os command
    - stdout : standard output of os command.
    - stderr : standard error of os command
    - id : same as the value of id member of the request object
    - errorcode : a number that indicates the error type that occurred.
        - 1 : json parse error
        - 2 : invalid request
        - 3 : invalid os command
        - 4 : internal server error
