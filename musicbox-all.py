#!/usr/bin/env python

import pygame
from pygame import *
import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(13, GPIO.IN)

mixer.pre_init(frequency=22500, size=-16, channels=1, buffer=4096)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((32, 32), 0, 32)

s1 = pygame.mixer.Sound('j01.wav')
s2 = pygame.mixer.Sound('j02.wav')
s3 = pygame.mixer.Sound('j03.wav')
s4 = pygame.mixer.Sound('j04.wav')
s5 = pygame.mixer.Sound('j05.wav')
s6 = pygame.mixer.Sound('j06.wav')
s7 = pygame.mixer.Sound('j07.wav')
s8 = pygame.mixer.Sound('j08.wav')

s1p = False
s2p = False
s3p = False
s4p = False
s5p = False
s6p = False
s7p = False
s8p = False


while True:

  if (GPIO.input(23) == False and s1p == False):
    s1.stop()
    s1.play(loops=-1)
    s1p = True
  else
    s1.fadeout()

  if (GPIO.input(24) == False and s2p == False):
    s2.stop()
    s2.play(loops=-1)
    s2p = True
  else
    s2.fadeout()
    s2p = False

  if (GPIO.input(25) == False and s3p == False):
    s3.stop()
    s3.play(loops=-1)
    s3p = True
  else
    s3.fadeout()
    s3p = False

  if (GPIO.input(12) == False and s4p == False):
    s4.stop()
    s4.play(loops=-1)
    s4p = True
  else
    s4.fadeout()
    s4p = False

  if (GPIO.input(16) == False and s5p == False):
    s5.stop()
    s5.play(loops=-1)
    s5p = True
  else
    s5.fadeout()
    s5p = False

  if (GPIO.input(20) == False and s6p == False):
    s6.stop()
    s6.play(loops=-1)
    s6p = True
  else
    s6.fadeout()
    s6p = False

  if (GPIO.input(21) == False and s7p == False):
    s7.stop()
    s7.play(loops=-1)
    s7p = True
  else
    s7.fadeout()
    s8p = False

  if (GPIO.input(26) == False and s8p == False):
    s8.stop()
    s8.play(loops=-1)
    s8p = True
  else
    s8.fadeout()
    s8p = False

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key==K_ESCAPE:
        pygame.mixer.stop()
	    pygame.quit()
	    sys.exit()
  pygame.display.update()
