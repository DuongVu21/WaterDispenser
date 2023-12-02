import RPi.GPIO as GPIO
import time

class SV():
    def __init__(self, pin = 26):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def open(self):
        GPIO.output(self.pin, GPIO.LOW)

    def close(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def cleanUp():
        GPIO.cleanup()

if __name__ == "__main__":
    SV_test = SV(21)
    SV_test.open()
    time.sleep(1)
    SV_test.close()
    # while True:
    #     SV_test.open()
    #     time.sleep(1)
    #     SV_test.close()
    #     time.sleep(1)