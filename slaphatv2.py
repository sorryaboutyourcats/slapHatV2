from __future__ import division
from time import sleep
import RPi.GPIO as GPIO

import curses
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm=GPIO.PWM(03, 50)
pwm.start(0)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(1)
screen.keypad(True)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

try:
        while True:  
            GPIO.setmode(GPIO.BOARD)
            char = screen.getch()
            print char
            if char == ord('q'):
                break
            elif char == ord('1'):
                print "out"
                SetAngle(86)
                time.sleep(.1)
            elif char == ord('2'):
                print "in"
                SetAngle(85)
                time.sleep(.1)
            elif char == ord('3'):
                print "slap"
                SetAngle(84)
                time.sleep(.1)
            elif char == ord('4'):
                print "3 slaps"
                for x in range(0,3):
                  SetAngle(120)
                  time.sleep(.5)
                  SetAngle(120)
                  time.sleep(.5)
                time.sleep(0.1)
            elif char == ord('5'):
                print "long slap"
                #not doing for continuous
                time.sleep(5)
                #not doing for continuous
                time.sleep(0.1)
            elif char == ord('6'):
                print "50 fast slaps"
                for x in range(0,50):
                  SetAngle(240)
                  time.sleep(.4)
            elif char == ord('7'):
                print "100 fast slaps"
                for x in range(0,100):
                  SetAngle(360)
                  time.sleep(.4)
            else:
                print "stop"
             
finally:
    pwm.stop()
    GPIO.cleanup()
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()