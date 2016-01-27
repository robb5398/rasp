# On and Off of one led

# turning on and off lED on numer 17 and 22 on T shape device

import RPi.GPIO as GPIO
import time

def led_on(n):
    GPIO.setmode(GPIO.BCM)      #BCM->broadcom
    GPIO.setwarnings(False)     # optional
    GPIO.setup(n,GPIO.OUT)     #17 for setting 17 no in breadboaded connected
                                #device, out for using out function for that
                                #17 no.
    
    GPIO.output(n,GPIO.HIGH)   # to turn on


def led_off(n):
    GPIO.setmode(GPIO.BCM)      #BCM->broadcom
    GPIO.setwarnings(False)     # optional
    GPIO.setup(n,GPIO.OUT)     #17 for setting 17 no in breadboaded connected
                                #device, out for using out function for that
                                #17 no.
    
    GPIO.output(n,GPIO.LOW)   # to turn off

for i in range(10):

    n = [17, 22]
    led_on(n[0])
    time.sleep(0.2)
    led_off(n[0])
    time.sleep(0.05)
    led_on(n[1])
    time.sleep(0.2)
    led_off(n[1])
    time.sleep(0.05)

#led_of()
