import socket
import os
from _thread import *
from datetime import datetime

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2005

ServerSideSocket.bind((host, port))
ServerSideSocket.listen(10)

def producer_client(connection):
    data = connection.recv(1024).decode()
    topic = data
    if os.path.exists("broker2/" + topic) == False:
        os.mkdir("broker2/" + topic)
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("broker2/" + topic + "/partition2.txt", "a") as f:
            f.write(data + " " + dt_string + "\n")
        with open("broker1/" + topic + "/partition2_replication.txt", "a") as f1:
            f1.write(data + " " + dt_string + "\n")
        with open("broker3/" + topic + "/partition2_replication.txt", "a") as f2:
            f2.write(data + " " + dt_string + "\n")    
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    client_type = Client.recv(1024).decode()
    if client_type == "producer":
        start_new_thread(producer_client, (Client, ))