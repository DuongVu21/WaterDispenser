#Libraries
import RPi.GPIO as GPIO
import time


class UsSensor():
    def __init__(self, triggerPin = 18, echoPin = 24):

        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
 
        #set GPIO Pins
        self.GPIO_TRIGGER = triggerPin
        self.GPIO_ECHO = echoPin
 
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
 
    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
 
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
 
        return distance

    def cleanUp():
        GPIO.cleanup()
 
if __name__ == '__main__':
    sensor = UsSensor()
    try:
        while True:
            dist = sensor.getDistance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor.cleanUp()

#This is UTW