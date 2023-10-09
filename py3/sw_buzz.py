import RPi.GPIO as GPIO

buzzPin = 17
buttPin = 18

global oldSw

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzPin, GPIO.OUT)
    GPIO.setup(buttPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setwarnings(False)
    oldSw = GPIO.HIGH
    
def loop():
    while True:
        newSw = GPIO.input(buttPin)
        if oldSw==newSw:
            GPIO.output(buzzPin, newSw)
            print("buzzer status changed >>")
            oldSw = newSw

def destroy():
    GPIO.cleanup()
    
if __name__=='__main__':
    print("Program start")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        