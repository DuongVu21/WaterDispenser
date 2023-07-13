
from socket_client import ClientCommunicator
from flask import Flask, render_template, Response
import threading

message_communicator = ClientCommunicator(dataType="message",host= "10.247.169.31", port = 28910)
message_communicator.send_message("R,0.25,5,G,4,4,Y,6,4")

#Look for refresh rate 