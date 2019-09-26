#!/usr/bin/env python

import cgi
import cgitb
import time
import RPi.GPIO as GPIO

print('Content-type: text/html; charaset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('digree')
print('<input type="number" name="digree" value="0">')
print('<input type="submit" value="revolution">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

BOTTOM, MIDDLE, TOP = 0.5, 1.44, 2.4
def setservo(dig):
    pal = 0
    if dig == 0:
        pal = MIDDLE
    elif dig < 0:
        k = (MIDDLE - BOTTOM)/90
        pal = MIDDLE + k*dig
    elif dig > 0:
        k = (TOP - MIDDLE)/90
        pal = MIDDLE + k*dig
    
    servo.ChangeDutyCycle(pal/20*100)
    time.sleep(0.5)
    

form = cgi.FieldStorage()
value = form.getvalue("digree")

print(int(value))
setservo(int(value))

GPIO.cleanup()
