
from socket_server import ServerCommunicator
from flask import Flask, render_template, Response
import threading

IPAdr = "10.247.201.235"
port = 28710

# Create a server socket for sending and receiving messages
communicator = ServerCommunicator(IPAdr, port, "message")
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

