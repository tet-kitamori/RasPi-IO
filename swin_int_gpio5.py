#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

swPin = 5

def swon(gpioPin):
    if gpioPin == swPin:
        print('1', flush=True)
        print('0', flush=True)
    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(swPin, GPIO.FALLING, callback=swon, bouncetime=100)

try:
    print('0', flush=True)
    while True:
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()