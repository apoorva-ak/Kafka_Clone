import subprocess
import time
import os

process1 = subprocess.Popen(["python3", "broker1.py"])
process2 = subprocess.Popen(["python3", "broker2.py"])
process3 = subprocess.Popen(["python3", "broker3.py"])

os.mkdir("broker1")
os.mkdir("broker2")
os.mkdir("broker3")

while True:
    if process1.poll() is None:
        print("Broker 1 working")
    else:
        print("Broker 1 down")
        break
    if process2.poll() is None:
        print("Broker 2 working")
    else:
        print("Broker 2 down")
        break
    if process3.poll() is None:
        print("Broker 3 working")
    else:
        print("Broker 3 down")
        break
    time.sleep(5)

