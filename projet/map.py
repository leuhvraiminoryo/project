import pygame, sys
from pygame.locals import *
from constants import *
from utils import *





while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(autel, relativeCoordsToPixels(autel1.pos))
    highlight(autel1.pos,autel1.size)
    pygame.display.update()
    FPSCLOCK.tick(FPS)

