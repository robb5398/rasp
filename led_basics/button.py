import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.OUT)


while True:
	if GPIO.input(17) == False:
		GPIO.output(27,GPIO.HIGH)
		print("1")
		time.sleep(2)
		break
	if GPIO.input(17) == True:
		GPIO.output(27,GPIO.LOW)
		print("2")

time.sleep(2)
GPIO.output(22,GPIO.LOW)
