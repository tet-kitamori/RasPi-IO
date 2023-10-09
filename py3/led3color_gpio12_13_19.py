import sys
import pigpio

ledPin_R = 12
ledPin_G = 13
ledPin_B = 16

LED_PWM_FREQ = 8000
LED_PWM_RANGE = 100

pwmDutyR = float(sys.argv[1])
pwmDutyG = float(sys.argv[2])
pwmDutyB = float(sys.argv[3])

pi = pigpio.pi()
pi.set_mode(ledPin_R, pigpio.OUTPUT)
pi.set_mode(ledPin_G, pigpio.OUTPUT)
pi.set_mode(ledPin_B, pigpio.OUTPUT)

pi.set_PWM_frequency(ledPin_R, LED_PWM_FREQ)
pi.set_PWM_frequency(ledPin_G, LED_PWM_FREQ)
pi.set_PWM_frequency(ledPin_B, LED_PWM_FREQ)

pi.set_PWM_range(ledPin_R, LED_PWM_RANGE)
pi.set_PWM_range(ledPin_G, LED_PWM_RANGE)
pi.set_PWM_range(ledPin_B, LED_PWM_RANGE)

pi.set_PWM_dutycycle(ledPin_R, int(pwmDutyR * LED_PWM_RANGE))
pi.set_PWM_dutycycle(ledPin_G, int(pwmDutyG * LED_PWM_RANGE))
pi.set_PWM_dutycycle(ledPin_B, int(pwmDutyB * LED_PWM_RANGE))

