from ctypes.wintypes import SIZE
from pump import Pump
from solenoid_valve import SV
from weight_sensor import weightSensor, sensorPair
import time, sys

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

FLOWRATE = 29 # mL/s
UNITTIME = (1/FLOWRATE)*10

class Dispense():
    def __init__(self, volume):
        self.pump = Pump(26)
        self.sv1 = SV(20)
        self.sv2 = SV(21)
        self.dispenseVolume = volume #mL
        self.dispenseTime = self.dispenseVolume/FLOWRATE
        print("dispenseTime = %.3f" % (self.dispenseTime))
        self.btl1Vol = 0
        self.btl2Vol = 0
        self.setBtlLevel()
        self.crntVolTtl = self.btl1Vol + self.btl2Vol
        self.initVolTtl = self.crntVolTtl
        print("Current volume total = %.0f" % (self.crntVolTtl))
        self.deltaV = 0

    def start(self):
        if(self.btl1Vol > 1000):
            self.pump.on()
            self.sv1.open()
            print("Pumping from bottle 1")
            time.sleep(self.dispenseTime)
            self.pump.off()
            self.sv1.close()
        elif(self.btl2Vol > 1000):
            self.pump.on()
            self.sv2.open()
            print("Pumping from bottle 2")
            time.sleep(self.dispenseTime)
            self.pump.off()
            self.sv2.close()
        else:
            print("Bottles empty!")
        self.setBtlLevel()
        
            
    def setBtlLevel(self):
        wsPair1tmp = [20]
        wsPair2tmp = [20]
        for i in range(len(wsPair1tmp)):
            time.sleep(0.1)
            wsPair1tmp[i] = wsPair1.getWeight()
            wsPair2tmp[i] = wsPair2.getWeight()
        self.btl1Vol = sum(wsPair1tmp)/len(wsPair1tmp)
        self.btl2Vol = sum(wsPair2tmp)/len(wsPair2tmp)
        print("Bottle 1: %.0f" % (self.btl1Vol/1000) + " L")
        print("Bottle 2: %.0f" % (self.btl2Vol/1000) + " L")