#!/usr/bin/env python
"""
================================================
ABElectronics ADCDAC Pi 2-Channel ADC, 2-Channel DAC | DAC Write Demo

run with: python demo_dacwrite.py
================================================

this demo will generate a 1.5V p-p square wave at 1Hz
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import time
import RPi.GPIO as GPIO

import turtle
import math
import numpy as np
from bresenham import bresenham

try:
    from ADCDACPi import ADCDACPi
except ImportError:
    print("Failed to import ADCDACPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCDACPi import ADCDACPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
	
penpin = 17
# The lowest we can go, without deforming the Character is 0.23
sleepVariable = 0.5

GPIO.setup(penpin,GPIO.OUT) #pin down

def origin():
    penUp()
    print("Origin")
    adcdac = ADCDACPi(2)
    adcdac.set_dac_raw(1, 0)  # set the voltage on channel 1 to 1.5V
    adcdac.set_dac_raw(2, 0)   # set the voltage on channel 1 to 1.5V
    time.sleep(sleepVariable)

def drawLine(vxFrom, vyFrom, vxTo, vyTo):
    time.sleep(sleepVariable)
    adcdac = ADCDACPi(2)
    i = 0
    l = list(bresenham(vxFrom, vyFrom, vxTo, vyTo))
    while i < len(l):	
        print(l[i][0],l[i][1])
        adcdac.set_dac_raw(2, l[i][0])  
        adcdac.set_dac_raw(1, l[i][1])   
        i=i+1
        time.sleep(.0001)

def drawLogo2():
    origin()
    penDown()
    drawLine(0,0,0,1000)
    drawLine(0,1000,329,343)             
    drawLine(329,343,329,0)
    drawLine(329,0,0,0)
    time.sleep(sleepVariable)
    penUp()
    adcdac = ADCDACPi(2)
    adcdac.set_dac_raw(1, 2000)  # set the voltage on channel 1 to 1.5V
    adcdac.set_dac_raw(2, 0)
    penDown()
    time.sleep(sleepVariable)
    drawLine(0,2000,386,2000)
    drawLine(386,2000,1186,343)
    drawLine(1186,343,1000,0)
    drawLine(1000,0,0,2000)
    time.sleep(sleepVariable)
    penUp()
    time.sleep(sleepVariable)
    adcdac.set_dac_raw(1, 0)  # set the voltage on channel 1 to 1.5V
    adcdac.set_dac_raw(2, 1657)
    penDown()
    time.sleep(sleepVariable)
    drawLine(1657,0,1657,2000)
    drawLine(1657,2000,2000,2000)
    drawLine(2000,2000,2000,0)
    drawLine(2000,0,1657,0)
    time.sleep(sleepVariable)
    penUp()
    adcdac.set_dac_raw(1, 0)  # set the voltage on channel 1 to 1.5V
    adcdac.set_dac_raw(2, 2696)
    penDown()
    time.sleep(sleepVariable)
    drawLine(2696,0,2457,429)
    drawLine(2457,429,2943,429 )
    drawLine(2943,429, 2696,0 )
    time.sleep(sleepVariable)
    penUp()
    adcdac.set_dac_raw(1, 2300)  # set the voltage on channel 1 to 1.5V
    adcdac.set_dac_raw(2, 3000)


def penDown():
    time.sleep(1)
    GPIO.output(penpin, 1)
    time.sleep(1)
	
def penUp():
    time.sleep(1)
    GPIO.output(penpin,0)
    time.sleep(1)

def main():
    origin()
    drawLogo2()
    
        
if __name__ == "__main__":
    main()

 
