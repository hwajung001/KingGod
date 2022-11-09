import RPi.GPIO as GPIO
import time
import random
from random import seed
from random import randint

x=randint(-90,90)
y=randint(1,360)
button =10

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(button,GPIO.IN)
def loop():
	while True:
		button_state = GPIO.input(button)
		if button_state == False:
			
			print(x, y)
			while GPIO.input(button) == False:
				time.sleep(0.2)
def endprogram():
	GPIO.cleanup()
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		print("keyboard interrupt detected")
		endprogram()
