import pygame
from pygame import *
import sys
from gpiozero import Button
btn = Button(17)

mixer.pre_init(frequency=22500, size=-16, channels=1, buffer=4096)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400,400),0,32)

def hello():
	print('Hello')

btn.when_pressed = hello

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quite()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key==K_ESCAPE:
	pygame.quit()
	sys.exit()
      elif event.key==K_UP:
	s = pygame.mixer.Sound('j01.wav')
	ch = s.play()
  pygame.display.update()
