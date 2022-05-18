import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print(f" Listening on {bind_ip}, port= {bind_port}")

def handle_client(client_socket: socket.socket) -> None:
    """ Handle the client

    client_socket: the client ...
    """
    request = client_socket.recv(1024)
    print(f"recieved: {str(request)}")
    client_socket.send(b"BOB")
    client_socket.close()

while True:

    client, addr = server.accept()

    print(f"accepted connection from {addr[0]}, {addr[1]}")

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()