import pigpio
import time
import random

ledPins = [12, 13, 16]

LED_PWM_FREQ = 8000
LED_PWM_RANGE = 100

pi = pigpio.pi()
pi.set_mode(ledPins[0], pigpio.OUTPUT)
pi.set_mode(ledPins[1], pigpio.OUTPUT)
pi.set_mode(ledPins[2], pigpio.OUTPUT)
pi.set_PWM_frequency(ledPins[0], LED_PWM_FREQ)
pi.set_PWM_frequency(ledPins[1], LED_PWM_FREQ)
pi.set_PWM_frequency(ledPins[2], LED_PWM_FREQ)
pi.set_PWM_range(ledPins[0], LED_PWM_RANGE)
pi.set_PWM_range(ledPins[1], LED_PWM_RANGE)
pi.set_PWM_range(ledPins[2], LED_PWM_RANGE)

while True:
    rval=random.randint(0, LED_PWM_RANGE)
    gval=random.randint(0, LED_PWM_RANGE)
    bval=random.randint(0, LED_PWM_RANGE)
    
    pi.set_PWM_dutycycle(ledPins[0], rval)
    pi.set_PWM_dutycycle(ledPins[1], gval)
    pi.set_PWM_dutycycle(ledPins[2], bval)
    time.sleep(1)
        
        