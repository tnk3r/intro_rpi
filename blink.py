import time
import RPi.GPIO as GPIO

#setup rpi in Board and setup pin
LED = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 0)

while True:
    GPIO.output(LED, 1)
    time.sleep(0.5)
    GPIO.output(LED, 0)
