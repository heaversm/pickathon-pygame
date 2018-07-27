#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

while True:
    if (GPIO.input(19) == False):
      print('1')
    if (GPIO.input(26) == False):
      print('2')
    sleep(0.1);
