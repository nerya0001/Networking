# Python TCP Client A
import socket

name = 'lhost'
serverPort = 12345

BUFFER_SIZE = 1024

MESSAGE = input("ClientA: Enter message/ Enter exit: ")

aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aSocket.connect(name, serverPort)

while MESSAGE != 'exit':
    aSocket.send(MESSAGE.encode())
    data = aSocket.recv(BUFFER_SIZE)
    print("ClientA received data:", data)
    MESSAGE = input("ClientA: Enter message to continue/ Enter exit: ")

aSocket.close()