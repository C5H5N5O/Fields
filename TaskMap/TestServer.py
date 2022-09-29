import socket

s = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
port = 8000

s.bind((ip, port))
s.listen(1)

print(f"waiting for user to connect. host is: '{socket.gethostbyname(socket.gethostname())}'...")

user, addr = s.accept()

print("user connected")

while True:

    print(user.recv(2048).decode("utf-8"))