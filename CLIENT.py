# SERVER
import socket
HOST = '127.0.0.1'
PORT = 8080
s = socket.socket()
# s.bind((HOST, PORT))
# s.listen()
# print('Success')
# while True:
conn, address = s.accept()
data = conn.recv(4096)
clientId = data.decode()
conn.send(f'Hello {clientId}'.encode())
conn.close()

# CLIENT
# import socket
# HOST = '127.0.0.1'
# PORT = 8080
# s = socket.socket()
CLIENT_ID='Client1'
s=s.connect((HOST,PORT))
s.send(CLIENT_ID.encode())
data=s.recv(4096)
print(data.decode())
s.close()