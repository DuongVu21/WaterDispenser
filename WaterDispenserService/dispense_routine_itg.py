import RPi.GPIO as GPIO
from pump import Pump
from solenoid_valve import SV
import time, sys

global count
global start_counter
start_counter = 0
count = 0

def countPulse(channel):
    global count
    global start_counter
    if start_counter == 1:
        count += 1

class Dispense():
    def __init__(self, volume, pin = 19):
        self.pump = Pump()
        self.sv = SV()
        self.dispenseVolume = volume
        self.totalVolume = 0
        self.FLOW_SENSOR_GPIO = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    def start(self): 
        global start_counter
        global count
        GPIO.add_event_detect(self.FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)
        self.pump.on()
        self.sv.open()

        while self.totalVolume <= self.dispenseVolume:
            try:
                start_counter = 1
                time.sleep(1) #count pulses in 1 secs intervals
                start_counter = 0
                flow = (count / 98) # Pulse frequency (Hz) = 98Q, Q is flow rate in L/min.
                self.totalVolume = self.totalVolume + (flow/600)
                print("The flow is: %.3f Liter/min" % (flow))
                print("Dispensed: ", self.totalVolume, " L")
                count = 0

            except KeyboardInterrupt:
                print('\nkeyboard interrupt!')
                GPIO.cleanup()
                sys.exit()

        
        self.pump.off()
        self.sv.close()
 