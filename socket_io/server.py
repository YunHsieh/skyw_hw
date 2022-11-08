import socket
from . import contants


class Socket_Server():

    def __init__(self):
        pass

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((contants.HOST, contants.PORT))
        s.listen(5)

        print('server start at: %s:%s' % (contants.HOST, contants.PORT))
        print('wait for connection...')

        # received the connect
        self.conn, addr = s.accept()
        print('connected by ' + str(addr))

        indata = self.conn.recv(1024)
        print(indata.decode())

    def send_msg(self, value):
        self.conn.settimeout(60)
        self.conn.send(str(value).encode())
