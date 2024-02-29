from pump import Pump
from solenoid_valve import SV
from weight_sensor import weightSensor, sensorPair
import time, sys

FLOWRATE = 17.23 # mL/s

wSensor1 = weightSensor(19, 13, 103)
wSensor2 = weightSensor(6, 5, 103)
wSensor3 = weightSensor(0, 11, 530)
wSensor4 = weightSensor(9, 10, 850)
# wSensor5 = weightSensor(19, 13, 103)
# wSensor6 = weightSensor(19, 13, 103)
# wSensor7 = weightSensor(19, 13, 103)
# wSensor8 = weightSensor(19, 13, 103)
wsPair1 = sensorPair(wSensor1, wSensor2)
wsPair2 = sensorPair(wSensor3, wSensor4)
# wsPair3 = sensorPair(wSensor5, wSensor6)
# wsPair4 = sensorPair(wSensor7, wSensor8)

class Dispense():
    def __init__(self, volume):
        self.pump = Pump(26)
        self.sv2 = SV(20)
        self.sv1 = SV(21)
        # self.btl1Pre = wsPair1
        # self.btl2Pre = wsPair2
        self.crntVolTtl = wsPair1.getWeight() + wsPair2.getWeight()
        self.initVolTtl = self.crntVolTtl
        print("Current volume total = %.0f" % (self.crntVolTtl))
        self.dispenseVolume = volume #mL
        self.deltaV = 0

    def start(self): 
        
        self.pump.on()
        while(self.deltaV < self.dispenseVolume):
            btl1lvl = wsPair1.getWeight()
            #if ((self.btl1Pre - btl1lvl) > 20)
            btl2lvl = wsPair2.getWeight()
            self.crntVolTtl = btl1lvl + btl2lvl
            print("Current volume total = %.0f" % (self.crntVolTtl))
            if (btl1lvl >= 9000): #Bottle 1 not empty
                self.sv1.open()
                self.sv2.close()
                print("Current bottle 1 level = %.0f" % (btl1lvl))
            elif (btl2lvl >= 9000): #Bottle 2 not empty
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