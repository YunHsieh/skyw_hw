import time
import utils
import statistics

from threading import Thread
from socket_io import client as csocket, server as ssocket
from pipe_io import server as spipe
from shared_memory_io import server as sshared_memory, client as cshared_memory


socket_server = ssocket.Socket_Server()
pipe_server = spipe.Pipe_Server()

if __name__ == '__main__':
    #create a list of threads
    workers = [
        socket_server.start,
        csocket.start,
        pipe_server.start,
        sshared_memory.start,
        cshared_memory.start,
    ]
    for worker in workers:
        process = Thread(target=worker, args=())
        process.Daemon = True
        process.start()
        time.sleep(0.5)

    data = input('Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values:')
    data = utils.to_nums(data)
    socket_server.send_msg(statistics.mean(data))
    pipe_server.send_msg(statistics.median(data))
    sshared_memory.put_data(statistics.mode(data))
