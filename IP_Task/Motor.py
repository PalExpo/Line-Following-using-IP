import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Cytron:

	Dir = None
	P = None
	pwm = None
	dC = 0													#DutyCycle is declared that its integers..

	def __init__(self, Dir, P):
		self.Dir = Dir
		self.P = P
		GPIO.setup(self.Dir, GPIO.OUT)
		GPIO.setup(self.P, GPIO.OUT)
		self.pwm = GPIO.PWM(self.P, 1000)

	def wholeClk(self, dC = 50):
		GPIO.output(self.Dir, GPIO.HIGH)
		self.pwm.start(self.dC)

	def wholeAclk(self, dC = 50):
		GPIO.output(self.Dir, GPIO.LOW)
		self.pwm.start(self.dC)

	def stopp(self, dC = 0):
		self.pwm.stop()

