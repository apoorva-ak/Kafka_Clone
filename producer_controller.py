import subprocess

print("Enter number of producers:")
message = input(" -> ")

num = int(message)
i = 0
while (i != num):
    subprocess.call(['gnome-terminal', "--", "python3", "producer.py"])
    i += 1