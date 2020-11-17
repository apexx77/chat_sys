import socket

HEADER = 64
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

#Enter your local IP Address below
SERVER = "192.168.19.1"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg) :
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("HELLO WORLD")
input()
send("HELLO UNIVERSE")
input()
send("HELLO USER")
input()
send(DISCONNECT_MESSAGE)
