
from socket_server import ServerCommunicator
from flask import Flask, render_template, Response
import threading

erIp = "10.247.169.31"
NitroIP = "10.247.209.233"
port = 28910

communicator = ServerCommunicator(NitroIP, port, "message")
Exit = False

while Exit != True:
    amount = input("Enter amount: ")

    if amount == "0" or amount == "exit":
        Exit = True

    elif communicator.address != None and float(amount) > 0:
        
        communicator.send_message(amount)

