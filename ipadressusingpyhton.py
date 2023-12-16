import socket

hostname=input("Please enter a website address:")

print(f'The{hostname} IP Address is {socket.gethostbyname(hostname)}')