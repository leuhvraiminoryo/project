import pygame

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
autel = pygame.image.load('projet/images/autel.png')

#setup
FPS = 60
WX = 800
WY = 500
CAPTION = 'Préparez-vous à entrer dans Xak Tsaroth!!!'
FPSCLOCK = pygame.time.Clock()
BOXSIZE = 16
BGCOLOR = GRAY
DISPLAYSURF = pygame.display.set_mode((WX,WY))