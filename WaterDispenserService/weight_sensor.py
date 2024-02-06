import RPi.GPIO as GPIO
from hx711 import HX711
import time
import sys

class sensorPair():
    def __init__(self, weightSensor1, weightSensor2):
        self.weightSensor1 = weightSensor1
        self.weightSensor2 = weightSensor2
        
    def getWeight(self):
        combinWgt = self.weightSensor1.getWeight() + self.weightSensor2.getWeight()
        return combinWgt

class weightSensor():
    def __init__(self, dout = 5, pd_sck = 6, ref = 103):
        self.hx = HX711(dout, pd_sck)
        referenceUnit = ref

        # I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
        # Still need to figure out why does it change.
        # If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
        # There is some code below to debug and log the order of the bits and the bytes.
        # The first parameter is the order in which the bytes are used to build the "long" value.
        # The second paramter is the order of the bits inside each byte.
        # According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
        self.hx.set_reading_format("MSB", "MSB")

        # HOW TO CALCULATE THE REFFERENCE UNIT
        # To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
        # In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
        # and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
        # If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
        #hx.set_reference_unit(113)
        self.hx.set_reference_unit(referenceUnit)

        self.hx.reset()

        self.hx.tare()

        print("Tare done! Add weight now...")
        
        self.preVal = 0

    def getWeight(self):
        val = self.hx.get_weight(5)

        if (val < (self.preVal - 300)):
            val = (self.preVal + val)/2
        else:
            self.preVal = val
        
        self.hx.power_down()
        self.hx.power_up()
        
        return val
        
    def cleanAndExit(self):
        print("Cleaning...")

        GPIO.cleanup()
        
        print("Bye!")
        sys.exit()

if __name__ == "__main__":
    testSensor = weightSensor()
    while True:
        try:
            val = testSensor.getWeight()
            print(val)
            time.sleep(0.1)

        except (KeyboardInterrupt, SystemExit):
            testSensor.cleanAndExit()