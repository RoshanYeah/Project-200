import socket
from threading import Thread

nickname = input('Enter your nickname: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '127.0.0.1'
PORT = 8000

client_socket.connect((IP, PORT))

def receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred')
            client_socket.close()
            break

def write(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

receive_thread = Thread(target=receive, args=(client_socket,))
receive_thread.start()

write_thread = Thread(target=write, args=(client_socket,))
write_thread.start()
