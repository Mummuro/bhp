import socket

target_host = "127.0.0.1"
target_port = 1234


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"bob mitch")