import socket

class ClientComunicator():
    def __init__(self, dataType, host, port):
        self.dataType = dataType
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def __del__(self):
        if self.socket != None:
            self.socket.close()

    def get_data(self):
        if self.dataType == "image":
            return self.socket.recv(15000)
        elif self.dataType == "message":
            return self.socket.recv(1024).decode()


if __name__ == "__main__":
    message_communicator = ClientComunicator(dataType="message",host= "localhost", port = 12345)
    while True:
        print(message_communicator.get_data())

    #message_communicator = ClientComunicator(dataType="message", host= "DESKTOP-UTI5DR3", port = 12346)
    #while True:
    #    print(message_communicator.get_data())
