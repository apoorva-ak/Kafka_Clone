import socket
import os
import time

host = '127.0.0.1'
port = 2004

client_socket = socket.socket() 
client_socket.connect((host, port))

message = "consumer"
client_socket.send(message.encode())

print("Subscribe to a topic:")
message = input(" -> ")
while os.path.exists("broker1/" + message) == False:
    print("Invalid topic. Subscribe again:")
    message = input(" -> ")
client_socket.send(message.encode())

print("Enter the action to be performed:")
message = input(" -> ")
client_socket.send(message.encode())
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(data)

time.sleep(30)
client_socket.close()
