import RPi.GPIO as GPIO
import time

class Pump():
    def __init__(self, pin = 16):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def cleanUp():
        GPIO.cleanup()

if __name__ == "__main__":
    pump_test = Pump(26)
    pump_test.on()
    time.sleep(3)
    pump_test.off()
    pump_test.cleanUp