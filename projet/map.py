import pygame, sys
from pygame.locals import *
from constants import *

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

while True:
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update()
    FPSCLOCK.tick(FPS)