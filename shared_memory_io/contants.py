import socket
import uuid

HOST = socket.gethostbyname("localhost")
PORT = 3456
PASSWORD = str(uuid.uuid4()).encode()
