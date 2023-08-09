import os
import socket

host = '127.0.0.1'
port = 2004

host2 = '127.0.0.1'
port2 = 2005

host3 = '127.0.0.1'
port3 = 2006

client_socket = socket.socket() 
client_socket.connect((host, port))

client_socket2 = socket.socket() 
client_socket2.connect((host2, port2))

client_socket3 = socket.socket() 
client_socket3.connect((host3, port3))

message = "producer"
client_socket.send(message.encode())
client_socket2.send(message.encode())
client_socket3.send(message.encode())

print("Enter the topic:")
message = input(" -> ")
client_socket.send(message.encode())
client_socket2.send(message.encode())
client_socket3.send(message.encode())

i = 0

print("Enter the messages:")
message = input(" -> ")
while message.lower().strip() != "eof":
    if (i%3 == 0):
        client_socket.send(message.encode())
    elif (i%3 == 1):
        client_socket2.send(message.encode())
    else:
        client_socket3.send(message.encode())
    message = input(" -> ")
    i += 1

client_socket.close()
client_socket2.close()
client_socket3.close()