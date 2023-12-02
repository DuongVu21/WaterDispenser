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
        self.crntVolTtl = self.wSensor1.getWeight() + self.wSensor2.getWeight()
        self.initVolTtl = self.crntVolTtl
        print("Current volume total = %.0f" % (self.crntVolTtl))
        self.dispenseVolume = volume #mL
        self.deltaV = 0

    def start(self): 
        
        self.pump.on()
        while(self.deltaV < self.dispenseVolume):
            btl1lvl = self.wSensor1.getWeight()
            btl2lvl = self.wSensor2.getWeight()
            self.crntVolTtl = btl1lvl + btl2lvl
            if (self.btl1lvl >= 700): #Bottle 1 not empty
                self.sv1.open()
                print("Current bottle level = %.0f" % (self.btl1lvl))
            elif (self.btl2lvl >= 9200): #Bottle 2 not empty
                self.sv2.open()
                self.sv1.close()
                print("Current bottle level = %.0f" % (self.btl2lvl))
            else: #Bottle 2 empty
                self.sv2.close()
                self.deltaV = self.dispenseVolume
            self.deltaV = self.initVolTtl - self.crntVolTtl
            time.sleep(0.05)
            
        self.pump.off()
        self.sv1.close()
        self.sv2.close()
        
        return self.btlNum