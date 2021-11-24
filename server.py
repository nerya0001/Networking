from socket import *
import sys  # In order to terminate the program


try:
    # (AF_INET is used for IPv4 protocols) # (SOCK_STREAM) is used for TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)
    print('Socket successfully created')
except error as e:
    print('Socket creation failed with error %s' %(e))
host = '10.9.11.59'
port = 12345

# Bind the socket to server address and server port
serverSocket.bind((host, port))
print('socket binded to %s' %(port))
# Listen to at most 1 connection at a time
serverSocket.listen(1)
print('socket is listening')
# Prepare a sever socket

# Fill in start
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start #Fill in end
    print('got connection from', addr)

    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
       # Fill in start #Fill in end
        # Fill in start
        # HTTP response
        outputdata = []
        outputdata.append("HTTP/1.1 200 OK\r\n")  # Send one HTTP header line into socket
        outputdata.append("Content-Type: text/html\r\n\r\n")
        outputdata.append("<html><body>Hello World</body></html>\r\n\r\n")
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        outputdata = []
        outputdata.append("HTTP/1.1 404 Not Found\r\n")
        outputdata.append("Content-Type: text/html\r\n\r\n")
        outputdata.append("<html><body>404 Not Found</body></html>\r\n\r\n")
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Fill in start
        connectionSocket.close() # Close client socket
        # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data