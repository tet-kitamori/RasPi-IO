#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

ledPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        if input() == '0':
            GPIO.output(ledPin, GPIO.LOW)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()
        
