import socket
from . import contants
import utils
import statistics

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((contants.HOST, contants.PORT))
    s.listen(5)

    print('server start at: %s:%s' % (contants.HOST, contants.PORT))
    print('wait for connection...')

    # received the connect
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    indata = conn.recv(1024)
    print(indata.decode())

    conn.settimeout(60)
    data = input('Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values:')
    if not data:
        conn.send('0'.encode())

    data = utils.to_nums(data)
    if data == []:
        print('only number in your input')
        conn.send('0')

    conn.send(str(statistics.mean(data)).encode())
