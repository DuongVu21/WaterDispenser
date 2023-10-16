
from ast import Try
import socket, time
from socket_client import ClientCommunicator
from flask import Flask, render_template, Response
#from dispense_routine import Dispense
#from dispense_routine_itg import Dispense
from dispense_routine_time import Dispense
import threading

host= "10.247.218.105"
port = 28910

Exit = False
message_communicator = ClientCommunicator(host, port, "message")

while Exit != True:
    volume = float(message_communicator.recv_message())

    # End program if volume received is 0 or less
    if volume <= 0:
        Exit = True

    #Dispense water in 100mL increments
    else: 
        print("Dispensing %.3f L of water" % (volume))
        dispenseRoutine = Dispense(volume)
        dispenseRoutine.start()





        #while volume > 0:
        #    if (volume > 0.1):
        #        dispenseRoutine = Dispense(0.1)
        #        dispenseRoutine.start()
        #        volume -= 0.1
        #    else:
        #        dispenseRoutine = Dispense(volume)
        #        dispenseRoutine.start()
        #        volume = 0
        #    time.sleep(1) # Pause for 1 second in-between












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