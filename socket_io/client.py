import socket
from . import contants

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((contants.HOST, contants.PORT))
        s.send(b'Client1 is ready')
        print(s.recv(1024).decode())
