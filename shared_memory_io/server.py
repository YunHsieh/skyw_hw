from multiprocessing.managers import BaseManager
from collections import defaultdict
from queue import Queue
import threading
from . import contants


class QueueManager(BaseManager): pass


def server_manager():
    return QueueManager(
        address=(contants.HOST, contants.PORT), 
        authkey=contants.PASSWORD
    )


def send_message(value):
    queues = defaultdict(Queue)
    if queues.get(value):
        return queues[value]
    else:
        return value


def start():
    """
    Use baseManager to create the server based on the socket
    """
    
    queues = defaultdict(Queue)
    m = server_manager()
    
    QueueManager.register('get_queue', callable=lambda value:queues[value])
    s = m.get_server()
    # A switch for stop
    stop_timer = threading.Timer(1, lambda:s.stop_event.set())
    QueueManager.register('stop', callable=lambda:stop_timer.start())
    # server run start
    s.serve_forever()


def put_data(data=1):
    """
    Create the connect to put the data in the memory
    """
    m = server_manager()
    m.connect()
    m.get_queue("mode").put(data)
