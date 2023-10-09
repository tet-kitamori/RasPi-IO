#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

swPin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
oldval = 99
try:
    while True:
        newval = GPIO.input(swPin)
        if oldval != newval:
            oldval = newval
            if newval == GPIO.LOW:
                print('1', flush=True)
            else:
                print('0', flush=True)
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    