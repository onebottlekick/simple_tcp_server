import socket

# server ipv4
HOST = '<own ipv4 address>'
PORT = 9090

# use tcp socket
# just connection socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(2)

while True:
    # communication socket
    communication_socket, address = server.accept()
    print(f"connetcted to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from client is: {message}")
    communication_socket.send("from server: I got your message".encode('utf-8'))    
    communication_socket.close()
    print(f"connection with {address} ended")
    break