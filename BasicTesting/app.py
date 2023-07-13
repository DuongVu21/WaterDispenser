
from led_routine import LEDRoutine
from socket_server import ServerCommunicator
from flask import Flask, render_template, Response
import threading

erIp = "10.247.169.31"
port = 28910

communicator = ServerCommunicator(erIp, port, "message")

while True:

    if communicator.address != None:
        routine = (communicator.recv_message()).split(",")
        
        for i in range(2, int(len(routine)), 3):
            color = routine[i-2]
            frequency = float(routine[i-1])
            duration = int(routine[i])
            tRoutine = LEDRoutine(color, frequency, duration)
            tRoutine.start()
            print ("Blinking " + color + " at " + str(frequency) + " Hz for " + str(duration) + " seconds")

    break

