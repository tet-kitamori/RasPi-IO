#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

ledPin = 23
PWMFREQ = 50
PWMINIT = 0.0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)

pwm = GPIO.PWM(ledPin, PWMFREQ)
pwm.start(PWMINIT)

try:
    while True:
        pwmval = float(input())
        pwm.ChangeDutyCycle(pwmval)
except KeyboardInterrupt:
    GPIO.cleanup()