#!/usr/bin/env python

def p_A(gridOffset):
	print("A")
	gridValue=(gridOffset*120)
	print ("VALUE ", gridValue)
	
	adcdac = ADCDACPi(2)
	adcdac.set_dac_raw(1, 0) 
	adcdac.set_dac_raw(2, 0+gridValue) 
	time.sleep(sleepVariable)
	
	penDown()
	# line from 1 to 2
	adcdac.set_dac_raw(1, 200)  
	adcdac.set_dac_raw(2, 50+gridValue)   
	time.sleep(sleepVariable)
	
	# line from 2 to 3
	adcdac.set_dac_raw(1, 0)  
	adcdac.set_dac_raw(2, 100+gridValue)  
	time.sleep(sleepVariable)
	penUp()
	adcdac.set_dac_raw(1, 100)  
	adcdac.set_dac_raw(2, 25+gridValue)   
	time.sleep(sleepVariable)
	penDown()
	adcdac.set_dac_raw(1, 100)  
	adcdac.set_dac_raw(2, 75+gridValue)   
	time.sleep(sleepVariable)
	penUp()