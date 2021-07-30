import socket

# target server ip
HOST = '<target ip address>'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
message = input("enter message: ")
socket.send(message.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))