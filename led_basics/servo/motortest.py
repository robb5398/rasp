import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

motor = 22

GPIO.setup(motor, GPIO.OUT)

print("Turning Forward")

GPIO.output(motor,GPIO.HIGH)

sleep(10)

print("TUrning back")
GPIO.output(motor,GPIO.LOW)

print("stop")

GPIO.cleanup()

