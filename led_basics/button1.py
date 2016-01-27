import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(22) == GPIO.LOW):
		print("switch pressed")
		break
GPIO.cleanup()

