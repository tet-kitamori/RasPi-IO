#!/usr/bin/env python3

pwm = 0.0
PWM_MIN = 0.0
PWM_MAX = 100.0
PWM_STEP = 10.0

print(pwm, flush=True)
try:
    while True:
        if input() == '1':
            pwm += PWM_STEP
            if pwm > PWM_MAX:
                pwm = PWM_MIN
            print(pwm, flush=True)
except KeyboardInterrupt:
    pass
