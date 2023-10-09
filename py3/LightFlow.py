#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

ledPins = [22, 23, 24, 27, 5, 6, 20, 21] 

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.output(ledPins, GPIO.LOW)

def ledLoop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
            
def destroy():
    GPIO.cleanup()
    
if __name__== '__main__':
    print('Program is starting..')
    setup()
    
    try:
        ledLoop()
            
    except KeyboardInterrupt:
        destroy()
    