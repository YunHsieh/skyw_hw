from threading import Thread
from socket_io import client as csocket, server as ssocket
from pipe_io import server as spipe
from shared_memory_io import server as sshared_memory, client as cshared_memory
import time


#create a list of threads
workers = [
    ssocket.start,
    csocket.start,
    spipe.start,
    sshared_memory.start,
    sshared_memory.put_data,
    cshared_memory.start,
]
for worker in workers:
    process = Thread(target=worker, args=())
    process.Daemon = True
    process.start()
    time.sleep(0.5)
