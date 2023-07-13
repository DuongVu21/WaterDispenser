from pickle import TRUE
import RPi.GPIO as GPIO
import time, sys

class FlowMeter():
    def __init__(self, pin = 19):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        self.rate_cnt = 0
        self.tot_cnt = 0
        self.time_zero = 0.0
        self.time_start = 0.0
        self.time_end = 0.0
        self.gpio_last = 0
        self.pulses = 0
        self.constant = 0.0001863 #L/rev

    def getFlowRate(self):
        self.rate_cnt = 0
        self.pulses = 0
        self.time_start = time.time()
        while self.pulses <= 0:
            self.gpio_cur = GPIO.input(self.pin)
            if self.gpio_cur != 0 and self.gpio_cur != self.gpio_last:
                self.pulses += 1
            self.gpio_last = self.gpio_cur
            try: 
                None
            except KeyboardInterrupt:
                GPIO.cleanup()
                print ("Keyboard interupt exit.")
                sys.exit()
        self.rate_cnt += 1
        self.tot_cnt += 1
        self.time_end = time.time()
        self.flowRate = self.rate_cnt * self.constant/(self.time_end - self.time_start) #L/s
        self.totalVolume = self.tot_cnt * self.constant #L
        self.elapsedTime = time.time() - self.time_zero #secs
        print("Total pulse: ", self.tot_cnt)
        
        return self.flowRate, self.totalVolume, self.elapsedTime

if __name__ == "__main__":
    test_fm = FlowMeter()
    
    while TRUE:
        test_fm.getFlowRate()
        try: 
            None
        except KeyboardInterrupt:
            GPIO.cleanup()
            print ("Keyboard interupt exit.")
            sys.exit()