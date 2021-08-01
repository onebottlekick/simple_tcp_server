import threading
import socket

HOST = 'localhost'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
    
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left.\n'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while  True:
        client, address = server.accept()
        print(f'connected with {str(address)}')

        client.send('nickname'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname of the client is {nickname}')
        print(f'current clients: {nicknames}\n')

        broadcast(f'{nickname} joined'.encode('ascii'))

        client.send('connected to server\n'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

print('listening..')
receive()
