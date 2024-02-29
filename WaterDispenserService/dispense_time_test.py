from pump import Pump
from solenoid_valve import SV
import time, sys

FLOWRATE = 17.23 # mL/s

class Dispense():
    def __init__(self):
        self.pump = Pump(26)
        self.sv = SV(20)

    def start(self, stime): 
        self.pump.on()
        self.sv.open()
        time.sleep(stime)
        self.pump.off()
        self.sv.close()
        
if __name__ == "__main__":
    testDisp = Dispense()
    testDisp.start(10)