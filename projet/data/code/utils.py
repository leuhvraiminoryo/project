import pygame, sys, json
from pygame.locals import *
import data.code.classes as cl

#colors
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
ARED     = pygame.Color(255,   0,   0, a=50)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

#images
b_imgs = {
    'autel' : pygame.image.load('projet/data/images/autel.png'),
    'orb' : pygame.image.load('projet/data/images/orb.png'),
    #'residence' : pygame.image.load('projet/data/images/residence.png'),
    #'entrepot' : pygame.image.load('projet/data/images/entrepot.png'),
    'armurerie' : pygame.image.load('projet/data/images/armurerie.png'),
    #'decoration' : pygame.image.load('projet/data/images/decoration.png')
}

#setup
FPS = 20
BOXSIZE = 32
WX = BOXSIZE*20
WY = BOXSIZE*20
CAPTION = 'Préparez-vous à entrer dans Xak Tsaroth!!!'
FPSCLOCK = pygame.time.Clock()

BGCOLOR = GRAY
DISPLAYSURF = pygame.display.set_mode((WX,WY))


def relativeCoordsToPixels(coords,cor_x=(WX/2),cor_y=(WY/2)):
    x,y = coords
    return ((x*BOXSIZE)+cor_x,(y*BOXSIZE)+cor_y)

def pixelsToRelativeCoords(coords,cor_x=(WX/2),cor_y=(WY/2)):
    x,y = coords
    return (round((x-cor_x)/BOXSIZE),round((y-cor_y)/BOXSIZE))

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

def getBuildRect(pos,size,cor_pos=-1,cor_size=2,cor_r_pos_x=WX/2,cor_r_pos_y=WY/2):
    x,y = relativeCoordsToPixels(pos,cor_r_pos_x,cor_r_pos_y)
    sizex, sizey = size[0]*BOXSIZE,size[1]*BOXSIZE
    rect = pygame.Rect(x+cor_pos,y+cor_pos,sizex+cor_size,sizey+cor_size)
    return rect

def blitBuilding(building,fade=0):
    img = b_imgs[building.type]
    DISPLAYSURF.blit(img, relativeCoordsToPixels(building.pos))

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

def showTranspaRed(building):
    size = relativeCoordsToPixels(building.size,0,0)
    s = pygame.Surface(size)
    s.set_alpha(150)
    s.fill(RED)
    DISPLAYSURF.blit(s,relativeCoordsToPixels(building.pos))

def drawGrid():
    for x in range(0, WX, BOXSIZE):
        for y in range(0, WY, BOXSIZE):
            rect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)

def showGrid():
    for x in range(WX):
        for y in range(WY):
            rect = getBuildRect((x,y),(1,1),0,0,0,0)
            pygame.draw.rect(DISPLAYSURF,RED,rect,width=1)

def toPlace(building,mouse_pos):
    drawGrid()
    sizex,sizey = building.size
    building.pos = pixelsToRelativeCoords(mouse_pos,WX/2+(BOXSIZE*sizex/2),WY/2+(BOXSIZE*sizey/2))
    blitBuilding(building,)
