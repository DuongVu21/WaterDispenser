from led import LED
import time
import RPi.GPIO as GPIO
import ultrasonic_ranger as usr

MIN_TO_SEC = 60

class LEDRoutine():
	def __init__(self, color, frequency, duration):
		if color == "R":
			self.pin = 21

		elif color == "G":
			self.pin = 20

		elif color == "Y":
			self.pin = 16

		else: 
			self.pin = 12

		self.halfPeriod = 0.5/frequency
		self.rep = int(duration / (self.halfPeriod * 2))
		self.remainder = duration % (self.halfPeriod * 2)
		self.lt = LED(self.pin)

	def start(self):
		for i in range(self.rep):
			self.lt.on()
			print("LED on")
			time.sleep(self.halfPeriod)
			self.lt.off()
			print("LED off")
			time.sleep(self.halfPeriod)
			
			if ((i == (self.rep-1)) & (self.remainder > 0)):
				self.lt.on()
				print("LED on")
				if (self.remainder >= self.halfPeriod):
					time.sleep(self.halfPeriod)
					self.lt.off()
					print("LED off")
					time.sleep(self.remainder - self.halfPeriod)
				else:
					time.sleep(self.remainder)
					self.lt.off()
					print("LED off")

if __name__ == "__main__":
	sensor = usr.UsSensor()
	red_led = LEDRoutine("R", 4, 0.25)
	green_led = LEDRoutine("G", 4, 0.25)
	yellow_led = LEDRoutine("Y", 4, 0.25)
	white_led = LEDRoutine("W", 4, 0.25)
	try:
		while True:
			dist = sensor.getDistance()
			print ("Measured Distance = %.1f cm" % dist)
			if ((dist > 50) | (dist < 10)):
				white_led.start()
			elif (dist > 40):
				green_led.start()
			elif (dist > 30):
				yellow_led.start()
			else:
				red_led.start()
	
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		sensor.cleanUp()

