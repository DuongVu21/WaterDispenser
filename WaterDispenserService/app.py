
from ast import Try
import socket, time
from socket_client import ClientCommunicator
from flask import Flask, render_template, Response
from dispense_routine import Dispense
#from dispense_routine_itg import Dispense
import threading

host= "10.247.209.233"
port = 28910

tries = 0

Exit = False
message_communicator = ClientCommunicator(host, port, "message")

while Exit != True:
    volume = 0
    
    try:
        volume = float(message_communicator.recv_message())
    except socket.error:
        tries+=1
        time.sleep(1)

    if volume > 0:
        dispenseRoutine = Dispense(volume)
        dispenseRoutine.start()
        tries = 0

    if tries >= 10:
        Exit = True












#import qr_scanner as qr

#cam = qr.QrScanner(0)

## initializing list
#user_list = ['Alex', 'Trung', 'Duong']

#while True:
#    _, data, frame = cam.get_frame()

#    print (data)
#    # Check if substring is part of List of Strings
#    res=False
#    for i in range(len(user_list)):
#        if(data == user_list[i]):
#            res=True
#    print(res)

#    if res:
#        print("Hello " + data)
#        break