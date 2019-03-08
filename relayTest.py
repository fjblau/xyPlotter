#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import json

pins = [4,17,27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

arr = []

for x in range(0,4) :
        print ('on: ',x)
        GPIO.setup(pins[x],GPIO.OUT)
        GPIO.output(pins[x],1)
        time.sleep(1)
        print('off: ', x)
        GPIO.output(pins[x],0)
        time.sleep(1)

