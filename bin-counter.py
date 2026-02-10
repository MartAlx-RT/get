import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 9
GPIO.setup(up, GPIO.IN)
down = 10
GPIO.setup(down, GPIO.IN)

sleep_time = 0.2

counter = 0

while True:
    if(GPIO.input(up) > 0):
        counter += 1
    if(GPIO.input(down) < 0):
        counter -= 1

    if(counter < 0 or counter > 7):
        counter = 0

    GPIO.output(leds, dec2bin(num))
