import subprocess

print("Enter number of consumer:")
message = input(" -> ")

num = int(message)
i = 0
while (i != num):
    subprocess.call(['gnome-terminal', "--", "python3", "consumer.py"])
    i += 1