import socket

class ClientCommunicator():
    def __init__(self, host = 'localhost', port = '12345', dataType = 'message'):
        self.dataType = dataType
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def __del__(self):
        if self.socket != None:
            self.socket.close()

    def send_message(self, message):
        if (self.dataType == "message"):
            self.socket.send(message.encode())
        if (self.dataType == "image"):
            self.socket.sendall(message.encode())

    def recv_message(self):
        if self.dataType == "image":
            return self.socket.recv(15000)
        elif self.dataType == "message":
            return self.socket.recv(1024).decode()


if __name__ == "__main__":
    message_communicator = ClientComunicator(dataType="message",host= "localhost", port = 12345)

    command = message_communicator.recv_message()[:2];

    if command == "On":
        print("1")

    #while True:
    #    print(message_communicator.get_data())

    #message_communicator = ClientComunicator(dataType="message", host= "DESKTOP-UTI5DR3", port = 12346)
    #while True:
    #    print(message_communicator.get_data())
