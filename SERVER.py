# SERVER
import socket
HOST = '127.0.0.1'
PORT = 8080
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
print('Success')
while True:
    conn, address = s.accept()
    data = conn.recv(4096)
    clientId = data.decode()
    print(clientId)
    conn.send(f'Hello {clientId}'.encode())
    conn.close()