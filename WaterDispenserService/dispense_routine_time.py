from pump import Pump
from solenoid_valve import SV
import time, sys

FLOWRATE = 17.23 # mL/s

class Dispense():
    def __init__(self, volume):
        self.pump = Pump(14)
        self.sv = SV()
        self.dispenseVolume = volume * 1000 # L to mL
        self.dispenseTime = self.dispenseVolume/FLOWRATE
        print("dispenseTime = %.3f" % (self.dispenseTime))

    def start(self): 
        self.pump.on()
        self.sv.open()
        time.sleep(self.dispenseTime)
        self.pump.off()
        self.sv.close()