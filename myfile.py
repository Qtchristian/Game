import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello')

setDisplay.fill(purple)


pygame.draw.circle(setDisplay,red, (50,50),20,10)\



while True:
	for event in pygame.event.get():
	  print event
	  if event.type == QUIT:
		pygame.quit()
		sys.exit()

	pygame.display.update()
