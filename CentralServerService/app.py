
from socket_server import ServerCommunicator
from flask import Flask, render_template, Response
import threading

erIp = "10.247.169.31"
NitroIP = "10.247.194.157"
port = 28710

# Create a server socket for sending and receiving messages
communicator = ServerCommunicator(NitroIP, port, "message")
Exit = False

# While loop to keep program running
while Exit != True:
    amount = input("Enter amount: ")

    # enter 0 or exit to end program
    if amount == "0" or amount == "exit":
        communicator.send_message("-1")
        Exit = True

    # send message if amount is positive
    elif float(amount) > 0:
        
        communicator.send_message(amount)

