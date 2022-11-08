from threading import Thread
from socket_io import client as csocket, server as ssocket
from pipe_io import server as spepe


if __name__ == '__main__':
    #create a list of threads
    workers = [
        ssocket.start,
        csocket.start,
        spepe.start,
    ]
    for woker in workers:
        process = Thread(target=woker, args=())
        process.start()
