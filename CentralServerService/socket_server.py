import socket

class ServerCommunicator():
    def __init__(self, host = 'localhost', port = 12345, dataType = 'message'):
        self.dataType = dataType
        self.host = host
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        print("Listening...")
        self.conn, self.address = self.s.accept()
        print("Connected")
            
    def __del__(self):
        if self.conn != None:
            self.conn.close()

    def send_message(self, message):
        if (self.dataType == "message"):
            self.conn.send(message.encode())
        if (self.dataType == "image"):
            self.conn.sendall(message.encode())

    def recv_message(self):
        if self.dataType == "image":
            return self.conn.recv(15000)
        elif self.dataType == "message":
            return self.conn.recv(1024).decode()


if __name__ == "__main__":
    communicator = ServerCommunicator(dataType="image", host="localhost", port=12345)
    
    communicator.send_message("On")
