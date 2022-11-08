from .server import server_manager
import statistics
import time

def start():
    try:
        m = server_manager()
        m.connect()
        print('Client3 is ready')
    except Exception as e:
        raise 

    # listen server until get data
    while True:
        data = m.get_queue("mode").get()
        if data:
            print(f'Mode is {statistics.mode([1,2,3])}')
            m.stop()
            break
        time.sleep(0.1)
