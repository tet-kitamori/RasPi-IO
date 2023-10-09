import sys
import pigpio

ledPin = 12
LED_PWM_FREQ = 8000
pwmDuty = float(sys.argv[1])

pi = pigpio.pi()
pi.set_mode(ledPin, pigpio.OUTPUT)

pi.hardware_PWM(ledPin, int(LED_PWM_FREQ), int(pwmDuty * 1e6))