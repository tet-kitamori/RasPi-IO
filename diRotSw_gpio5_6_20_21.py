#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

swPin1 = 5
swPin2 = 6
swPin4 = 20
swPin8 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(swPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(swPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(swPin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(swPin8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
oldval = 99
try:
    while True:
        val1 = GPIO.input(swPin1)
        val2 = GPIO.input(swPin2)
        val4 = GPIO.input(swPin4)
        val8 = GPIO.input(swPin8)
        newval = 0
        if val1 == GPIO.LOW:
            newval += 1
            
        if val2 == GPIO.LOW:
            newval += 2
            
        if val4 == GPIO.LOW:
            newval += 4
            
        if val8 == GPIO.LOW:
            newval += 8
         
        if oldval != newval:
            oldval = newval
            print(newval, flush=True)
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()