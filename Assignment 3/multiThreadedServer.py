from socket import *
from threading import Thread  # threads usage
import sys  # In order to terminate the program

class ServerThread(Thread):  # Creating the thread class.

    def __init__(self, ip: int, port: int):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("Added new socket thread for -> " + str(ip) + ":" + str(port))

    def run(self):
        while True:
            print('Ready to serve...')
            connection, addr = serverSocket.accept()  # obtaining established connection from the backlog queue.
            try:
                message = connection.recv(1024).decode()  # decoding the message to bits.
                filename = message.split()[1]
                f = open(filename[1:])

                # sending a basic message to our client, including HTTP Header :
                outputdata = []
                outputdata.append("HTTP/1.1 200 OK\r\n")
                outputdata.append("Content-Type: text/html; charset=utf-8\r\n\r\n")
                outputdata.append("<html><body>Hello World</body></html>\r\n\r\n")

                for i in range(0,
                               len(outputdata)):  # can use also send all instead, right now for this project using this.
                    connection.send(outputdata[i].encode())  # encoding bits to real language.
                connection.send("\r\n".encode())  # encoding bits to real language.

                connection.close()
            except IOError:
                # Send response message for file not found
                # the idea below is like the above, sending an error message if the name server is incorrect.
                outputdata = []
                outputdata.append('HTTP/1.1 404 Not Found\r\n')
                outputdata.append('Content-Type: text/html\r\n\r\n')
                outputdata.append('<html><head></head><body>404 Not Found</body></html>')
                for i in range(0,
                               len(outputdata)):  # can use also send all instead, right now for this project using this.
                    connection.send(outputdata[i].encode())  # encoding bits to real language.
                connection.send("\r\n".encode())  # encoding bits to real language.

                connection.close()


address = '10.9.11.59'
port = 12345

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((address, port))
threads = []

while True:
    serverSocket.listen(4)  # up to 4 clients can connect
    print("Waiting for connections from TCP clients...")
    (tcp_connection, (ip, port)) = serverSocket.accept()
    new_thread = ServerThread(ip, port)  # init a thread
    new_thread.start()  # start the thread.
    threads.append(new_thread)

