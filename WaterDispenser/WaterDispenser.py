import socket
import threading
import random


host = socket.gethostname()
host = 'localhost'
print('Host name: ' + host)
port = 28910

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(1)

class clientSocket:
    SENDMSG = 'Fulfilled'
    RECVMSG = 'Fulfilled' #'Wish'
    SENDLEN = len(SENDMSG)
    RECVLEN = len(RECVMSG)
    
    def __init__(self, sokt=None):
        if sokt is None:
            self.sokt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sokt = sokt

    def connect(self, host, port):
        self.sokt.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < self.SENDLEN:
            sent = self.sokt.send(str.encode(msg[totalsent:]))
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent += sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.RECVLEN:
            chunk = self.sokt.recv(min(self.RECVLEN - bytes_recd, self.RECVLEN))
            print(chunk)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


def handle_rq(conn):
    hdlport = random.randint(10000, 20000)
    hdlport = 12345
    handlersocket = clientSocket()
    handlersocket.connect(conn, hdlport)
    
    return

sendone = clientSocket()
sendone.connect(host, port)
sendone.mysend('Fulfilled')
print('Sent!')

while True:
    (conn, address) = serversocket.accept()
    hdl = threading.Thread(target=handle_rq(conn))
    hdl.start()