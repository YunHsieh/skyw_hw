from multiprocessing import Process, Pipe
import statistics
import utils

def reader(p_client):
    p_client.send('Client2 is ready')
    while True:
        msg = p_client.recv()    # Read from the output pipe
        if msg.lower() == 'exit':
            break
        print(msg)
    p_client.close()


def start():
    p_server, p_client = Pipe()
    reader_p = Process(target=reader, args=(p_client,))
    reader_p.daemon = True
    reader_p.start()    # Launch the reader process

    p_server.send(f'wait connect...')
    msg = p_server.recv()
    print(msg)

    data = input('Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values:')
    data = utils.to_nums(data)

    p_server.send(f'Median is {statistics.median(data)}')
    # A switch
    p_server.send('exit')
    p_server.close()
    reader_p.join()

if __name__ == '__main__':
    pass
