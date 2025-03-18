#import socket module
from socket import *
import os
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverHost = 'localhost'
recvBuffer = 1024
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

# MIME type dictionary
MIME_TYPES = {
    '.html': 'text/html; charset=UTF-8',
    '.htm': 'text/html; charset=UTF-8',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.css': 'text/css',
    '.js': 'application/javascript'
}

while True:
    # Establish the connection
    print('ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)  # Receive message from the client

        message = message.decode()
        filename = message.split()[1].split('?')[0]  # Extract the filename and remove the query string

        file_extension = os.path.splitext(filename)[1]  # Get file extension

        file_path = filename[1:]  # Remove the leading slash

        if file_extension in MIME_TYPES:  # Check if the file type is supported
            # Open files based on extension (image files in binary, others in text)
            if file_extension in ['.jpg', '.jpeg', '.png']:  # Open images in binary mode
                with open(file_path, 'rb') as f:
                    outputdata = f.read()
            else:  # Open other files (HTML, CSS, JS, etc.) in text mode with UTF-8 encoding
                with open(file_path, 'r', encoding='utf-8') as f:
                    outputdata = f.read()

            # Send HTTP header
            response = "HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: {MIME_TYPES[file_extension]}\r\n"
            response += "\r\n"  # Blank line after headers

            # Send response headers
            connectionSocket.send(response.encode())

            # Send the content of the file
            connectionSocket.send(
                outputdata.encode() if isinstance(outputdata, str) else outputdata)  # Send binary or text content
    except IOError:
        # Send response message for file not found
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(response.encode())
    finally:
        # Close client socket
        connectionSocket.close()
