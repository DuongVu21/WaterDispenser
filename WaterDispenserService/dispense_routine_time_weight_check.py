from pump import Pump
from solenoid_valve import SV
from weight_sensor import weightSensor, sensorPair
import time, sys

wSensor1 = weightSensor(19, 13, 103)
wSensor2 = weightSensor(6, 5, 103)
wSensor3 = weightSensor(0, 11, 103)
wSensor4 = weightSensor(9, 10, 103)
# wSensor5 = weightSensor(19, 13, 103)
# wSensor6 = weightSensor(19, 13, 103)
# wSensor7 = weightSensor(19, 13, 103)
# wSensor8 = weightSensor(19, 13, 103)
wsPair1 = sensorPair(wSensor1, wSensor2)
wsPair2 = sensorPair(wSensor3, wSensor4)
# wsPair3 = sensorPair(wSensor5, wSensor6)
# wsPair4 = sensorPair(wSensor7, wSensor8)

FLOWRATE = 16.67 # mL/s
UNITTIME = (1/FLOWRATE)*10

class Dispense():
    def __init__(self, volume):
        self.pump = Pump(26)
        self.sv = SV(20)
        self.dispenseVolume = volume #mL
        self.dispenseTime = self.dispenseVolume/FLOWRATE
        print("dispenseTime = %.3f" % (self.dispenseTime))
        self.wsPair1 = wsPair1
        self.wsPair2 = wsPair2
        self.btl1Pre = self.wsPair1
        self.btl2Pre = self.wsPair2
        self.crntVolTtl = self.wsPair1.getWeight() + self.wsPair2.getWeight()
        self.initVolTtl = self.crntVolTtl
        print("Current volume total = %.0f" % (self.crntVolTtl))
        self.deltaV = 0

    def start(self):
        while(self.deltaV < self.dispenseVolume):
            self.pump.on()
            self.sv.open()
            time.sleep(self.dispenseTime)
            self.pump.off()
            self.sv.close()