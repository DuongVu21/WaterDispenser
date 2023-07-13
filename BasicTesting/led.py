import RPi.GPIO as GPIO

class LED():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)


    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def cleanUp():
        GPIO.cleanup()

if __name__ == "__main__":
    LED_test = LED()
    LED_test.on
    #LED_test.off