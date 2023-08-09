import socket
import os
from _thread import *
from datetime import datetime

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004

ServerSideSocket.bind((host, port))
ServerSideSocket.listen(10)

def producer_client(connection):
    data = connection.recv(1024).decode()
    topic = data
    
    if os.path.exists("broker1/" + topic) == False:
        os.mkdir("broker1/" + topic)
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("broker1/" + topic + "/partition1.txt", "a") as f:
            f.write(data + " " + dt_string + "\n")
        with open("broker2/" + topic + "/partition1_replication.txt", "a") as f1:
            f1.write(data + " " + dt_string + "\n")
        with open("broker3/" + topic + "/partition1_replication.txt", "a") as f2:
            f2.write(data + " " + dt_string + "\n")
             
    connection.close()        

def consumer_client(connection):
    topic = connection.recv(1024).decode()
    cons_time = datetime.now()
    action = connection.recv(1024).decode()
    dict = {}

    if os.path.exists("broker1/" + topic + "/partition1.txt") == True:
        with open("broker1/" + topic + "/partition1.txt", "r") as file1:
            for line in file1:
                lst = line.strip().split(" ")
                time = lst.pop()
                date = lst.pop()
                msg = " ".join(lst)
                msg_time = datetime.strptime(date + " " + time , "%d/%m/%Y %H:%M:%S")
                dict[msg_time] = msg

    if os.path.exists("broker1/" + topic + "/partition2_replication.txt") == True:
        with open("broker1/" + topic + "/partition2_replication.txt", "r") as file1:
            for line in file1:
                lst = line.strip().split(" ")
                time = lst.pop()
                date = lst.pop()
                msg = " ".join(lst)
                msg_time = datetime.strptime(date + " " + time , "%d/%m/%Y %H:%M:%S")
                dict[msg_time] = msg

    if os.path.exists("broker1/" + topic + "/partition3_replication.txt") == True:
        with open("broker1/" + topic + "/partition3_replication.txt", "r") as file1:
            for line in file1:
                lst = line.strip().split(" ")
                time = lst.pop()
                date = lst.pop()
                msg = " ".join(lst)
                msg_time = datetime.strptime(date + " " + time , "%d/%m/%Y %H:%M:%S")
                dict[msg_time] = msg

    if action == "read from-beginning":
        for i in sorted(dict.keys()):
            msg = dict[i] + "\n"
            connection.send(msg.encode())

    if action == "read":
        for i in sorted(dict.keys()):
            if i > cons_time:
                msg = dict[i] + "\n"
                connection.send(msg.encode())
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    client_type = Client.recv(1024).decode()
    if client_type == "producer":
        start_new_thread(producer_client, (Client, ))
    elif client_type == "consumer":
        start_new_thread(consumer_client, (Client, ))