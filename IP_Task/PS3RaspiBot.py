from pygame import *
from Motor import *
from Base import *
from time import *

axisUpDown = 1
axisLeftRight = 0

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

global pwm
global forward
global left
global right
global backward
global clockwise
global antiClockwise
global hadEvent
global increase_pwm
global decrease_pwm

pwm = 50
forward = False
left = False
right = False
backward = False
clockwise = False
antiClockwise = False
increasePwm = False
decreasePwm = False

m_1 = Cytron(21, 23)
m_2 = Cytron(20, 24)
m_3 = Cytron(22, 11)
m_4 = Cytron(10, 9)

bot = Base(m_1, m_2, m_3, m_4)

def RemoteControl(events):

	global forward
	global left
	global right
	global backward
	global hadEvent
	global pwm
	global antiClockwise
	global clockwise
	global increasePwm
	global decreasePwm

	for event in events:
		if event.type == QUIT:
			quit()
		if joystick.get_button(6):
			pwm = 50
		if joystick.get_button(7):
			pwm = 80


		if joystick.get_button(15):
			bot.left()
		if joystick.get_button(16):
			bot.right()


		if (joystick.get_button(3) & joystick.get_button(13)):
			bot.upLeft()
		elif joystick.get_button(13):
			bot.forward()
		if (joystick.get_button(1) & joystick.get_button(13)):
			bot.upRight()
		elif joystick.get_button(13):
			bot.forward()
		if (joystick.get_button(3) & joystick.get_button(14)):
			bot.downLeft()
		elif joystick.get_button(14):
			bot.backward()
		if (joystick.get_button(1) & joystick.get_button(14)):
			bot.downRight()
		elif joystick.get_button(14):
			bot.backward()
		if (joystick.get_button(2) & joystick.get_button(13)):
			bot.clockWise()
		elif joystick.get_button(13):
			bot.forward()
		if (joystick.get_button(0) & joystick.get_button(14)):
			bot.clockWise()
		elif joystick.get_button(14):
			bot.backward()

GPIO.cleanup()