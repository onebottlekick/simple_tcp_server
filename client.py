import threading
import socket

nickname = input('nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nickname':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception:
            print('error occurred\n')
            client.close()
            break

def write():
    while True:
        input_m = input("")
        message = f'{nickname}: {input_m}' 
        if input_m == "break":
            client.send(f'{nickname} left'.encode('ascii'))
            return
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()