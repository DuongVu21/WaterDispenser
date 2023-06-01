import socket

class ServerCommunicator():
    def __init__(self, dataType,host, port):
        self.dataType = dataType
        self.host = host
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        self.conn, self.address = self.s.accept()
            
    def __del__(self):
        if self.conn != None:
            self.conn.close()

    def send_message(self, message):
        if (self.dataType == "message"):
            self.conn.send(message.encode())
        if (self.dataType == "image"):
            self.conn.sendall(message.encode())


if __name__ == "__main__":
    communicator = ServerCommunicator(dataType="image", host="localhost", port=12345)
    
    while True:
        communicator.send_message("Boo")

    # message_communicator = ServerCommunicator(dataType="message", host= "DESKTOP-UTI5DR3", port = 12346)
    # while True:
    #     number_of_people = random.randint(1,20)
    #     entry = random.randint(1,20)
    #     exit = random.randint(1,20)
    #     temp = random.randint(35,60)
    #     humidity = random.randint(50,70)
    #     message_communicator.send_message("{number_of_people},{entry},{exit},{temp},{humidity}".format(number_of_people = number_of_people, entry=entry, exit=exit, temp=temp, humidity=humidity))
    #     time.sleep(1)
