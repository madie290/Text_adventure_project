#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
serverHost = 'localhost'

recvBuffer = 1024
serverPort = 6789
serverSocket.bind(("", serverPort))
#Fill in end
serverSocket.listen(1)
while True:
    #Establish the connection
    print('ready to serve...')
    connectionSocket, addr =  serverSocket.accept()# Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) # accidentally wrote serversocket used
        # AI to help fix this error
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        request = "HTTP/1.1 200 OK\r\n\r\n" # used ai to add the \r\n
        connectionSocket.send(request.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
    # Send response message for file not found
    # Fill in start
        Request = "404 File Not Found\r\n\r\n"
        connectionSocket.send(Request.encode())
    # Fill in end
    # Close client socket
    # Fill in start
        connectionSocket.close()
    # Fill in end
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data