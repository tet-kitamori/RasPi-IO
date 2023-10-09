#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

ledPins = [22, 23, 24, 27]

leds = [[0,0,0,0], [1,0,0,0], [0,1,0,0], [1,1,0,0],
        [0,0,1,0], [1,0,1,0], [0,1,1,0], [1,1,1,0],
        [0,0,0,1], [1,0,0,1], [0,1,0,1], [1,1,0,1],
        [0,0,1,1], [1,0,1,1], [0,1,1,1], [1,1,1,1]]

GPIO.setmode(GPIO.BCM)


GPIO.setwarnings(False)
GPIO.setup(ledPins, GPIO.OUT)

try:
    while True:
        ledPatNum = int(input())
        ledPattern = leds[ledPatNum]
        
        for i in range(4):
            if ledPattern[i] == 0:
                GPIO.output(ledPins[i], GPIO.LOW)
            else:
                GPIO.output(ledPins[i], GPIO.HIGH)
            
            
except KeyboardInterrupt:
    GPIO.cleanup()