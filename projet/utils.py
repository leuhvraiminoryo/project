import pygame, sys
from pygame.locals import *
from constants import *
from buildings import *


def relativeCoordsToPixels(coords):
    x,y = coords
    return ((x*BOXSIZE)+(WX/2),(y*BOXSIZE)+(WY/2))

def terminateGame():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminateGame()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminateGame()
        pygame.event.post(event)

def highlight(pos,size):
    """Trace rectangle autours d'un objet
    pos relative en boites
    size relative en boites"""
    x,y = relativeCoordsToPixels(pos)
    sizex, sizey = size[0]*16,size[1]*16
    rect = pygame.Rect(x-1,y-1,sizex+2,sizey+2)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect, width=1)


autel1 = Building('autel',(0,0),(2,2))

