import sys
import pigpio

ledPin_R = 12

LED_PWM_FREQ = 8000
LED_PWM_RANGE = 100

pwmDutyR = float(sys.argv[1])

pi = pigpio.pi()
pi.set_mode(ledPin_R, pigpio.OUTPUT)

pi.set_PWM_frequency(ledPin_R, LED_PWM_FREQ)

pi.set_PWM_range(ledPin_R, LED_PWM_RANGE)

pi.set_PWM_dutycycle(ledPin_R, int(pwmDutyR * LED_PWM_RANGE))
