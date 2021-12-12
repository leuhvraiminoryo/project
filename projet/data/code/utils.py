import pygame, sys, json
from pygame.locals import *
import data.code.classes as cl

#colors
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

#images
b_imgs = {
    'autel' : pygame.image.load('projet/data/images/autel.png'),
    'orb' : pygame.image.load('projet/data/images/orb.png')
}

#setup
FPS = 60
WX = 800
WY = 500
CAPTION = 'Préparez-vous à entrer dans Xak Tsaroth!!!'
FPSCLOCK = pygame.time.Clock()
BOXSIZE = 32
BGCOLOR = GRAY
DISPLAYSURF = pygame.display.set_mode((WX,WY))


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

def getBuildRect(pos,size,cor_pos=-1,cor_size=2):
    x,y = relativeCoordsToPixels(pos)
    sizex, sizey = size[0]*BOXSIZE,size[1]*BOXSIZE
    rect = pygame.Rect(x+cor_pos,y+cor_pos,sizex+cor_size,sizey+cor_size)
    return rect

def highlight(pos,size):
    """Trace rectangle autours d'un objet
    pos relative en boites
    size relative en boites"""
    rect = getBuildRect(pos,size)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect, width=1)

def mouseOverBuilding(building,mouse_pos):
    rect = getBuildRect(building.pos,building.size,0,0)
    if rect.collidepoint(mouse_pos):
        return True
    return False
