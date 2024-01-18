from pump import Pump
from solenoid_valve import SV
from weight_sensor import weightSensor
import time, sys

FLOWRATE = 17.23 # mL/s

class Dispense():
    def __init__(self, volume, weightSensor1, weightSensor2):
        self.pump = Pump(26)
        self.sv2 = SV(21)
        self.sv1 = SV(20)
        self.wSensor1 = weightSensor1
        self.wSensor2 = weightSensor2
        self.btl1Pre = self.wSensor1
        self.btl2Pre = self.wSensor2
        self.crntVolTtl = self.wSensor1.getWeight() + self.wSensor2.getWeight()
        self.initVolTtl = self.crntVolTtl
        print("Current volume total = %.0f" % (self.crntVolTtl))
        self.dispenseVolume = volume #mL
        self.deltaV = 0

    def start(self): 
        
        self.pump.on()
        while(self.deltaV < self.dispenseVolume):
            btl1lvl = self.wSensor1.getWeight()
            #if ((self.btl1Pre - btl1lvl) > 20)
            btl2lvl = self.wSensor2.getWeight()
            self.crntVolTtl = btl1lvl + btl2lvl
            print("Current volume total = %.0f" % (self.crntVolTtl))
            if (btl1lvl >= 700): #Bottle 1 not empty
                self.sv1.open()
                self.sv2.close()
                print("Current bottle 1 level = %.0f" % (btl1lvl))
            elif (btl2lvl >= 8500): #Bottle 2 not empty
                self.sv2.open()
                self.sv1.close()
                print("Current bottle 2 level = %.0f" % (btl2lvl))
            else: #Bottle 2 empty
                self.sv1.close()
                self.sv2.close()
                self.deltaV = self.dispenseVolume
                print("Current bottle 2 level = %.0f" % (btl2lvl))
                self.dispenseVolume = 0
            self.deltaV = self.initVolTtl - self.crntVolTtl
            time.sleep(0.01)
            
        self.pump.off()
        self.sv1.close()
        self.sv2.close()