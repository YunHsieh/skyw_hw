from multiprocessing import Process, Pipe


class Pipe_Server():
    def __init__(self):
        pass

    def reader(self, p_client):
        p_client.send('Client2 is ready')
        while True:
            msg = p_client.recv()    # Read from the output pipe
            if msg.lower() == 'exit':
                break
            print(msg)
        p_client.close()

    def start(self):
        self.p_server, p_client = Pipe()
        self.reader_p = Process(target=self.reader, args=(p_client,))
        self.reader_p.daemon = True
        self.reader_p.start()    # Launch the reader process

        self.p_server.send(f'waiting connection...')
        msg = self.p_server.recv()
        print(msg)
    
    def send_msg(self, value):
        self.p_server.send(f'Median is {value}')
        # A switch
        self.p_server.send('exit')
        self.p_server.close()
        self.reader_p.join()
