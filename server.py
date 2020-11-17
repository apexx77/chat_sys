import socket
import threading

PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("Enter your name: ")
server_name = input()

#Handling the client connection
def handle_client(conn, addr) :
    print(f"[NEW CONNECTION] {addr} connected.")
    client_name = conn.recv(1024).decode(FORMAT)
    conn.send(server_name.encode(FORMAT))

    connected = True
    while connected :
        msg = conn.recv(1024).decode(FORMAT)
        if msg :
            if msg == DISCONNECT_MESSAGE :
                connected = False
                print(client_name, "Disconnected!")
                conn.send("YOU ARE SUCCESSFULLY DISCONNECTED!".encode(FORMAT))
            else :
                print(client_name, " :", msg)
                server_msg = input()
                conn.send(server_msg.encode(FORMAT))
    conn.close()

#Main Function
def start() :
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True :
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting.....")

start()
