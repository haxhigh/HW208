import socket
from  threading import Thread

IP_ADDRESS = "127.0.0.1"
port = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("starting")

    global port
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind(IP_ADDRESS,port)
    SERVER.listen(100)

    acceptConnections()

    print("Server started")

def acceptConnections():
    while True:
        global SERVER
        global clients

        client,addr = SERVER.accept()
        print(client,addr)