from threading import Thread
from socket_io import client, server


if __name__ == '__main__':
    #create a list of threads
    workers = [
        server.start,
        client.start
    ]
    for woker in workers:
        process = Thread(target=woker, args=())
        process.start()
