import socket

HEADER = 64
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

print("ENTER THE SERVER IP ADDRESS: ")
SERVER = input()

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("Enter your name: ")
host_name = input()
client.send(host_name.encode(FORMAT))
print("To Disconnect the server, type DISCONNECT")
server_name = client.recv(1024).decode(FORMAT)
connected = True
while connected :
    msg = input()
    client.send(msg.encode(FORMAT))
    if msg == DISCONNECT_MESSAGE :
        connected = False
    server_msg = client.recv(1024).decode(FORMAT)
    print(host_name, ">>", server_msg)


