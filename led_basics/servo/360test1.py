import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.warnings(False)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 25)

p.start(49)



try:
        while True:
                p.ChangeDutyCycle(50)
		print("wait started")
                time.sleep(2)
		print("wait ended")
                p.ChangeDutyCycle(12)
                time.sleep(2)
#		p.ChangeDutyCycle(25) # added code
#		time.sleep(1)	 # added
                p.ChangeDutyCycle(2)
                time.sleep(2)

except KeyboardInterrupt:
        GPIO.cleanup()
