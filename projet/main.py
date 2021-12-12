from data.code.utils import *

autel1 = cl.Building('autel',(0,0),(2,2))
orb1 = cl.Building('orb',(-1,1),(1,1))

list_buildings = [autel1,orb1]

while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    for building in list_buildings:
        DISPLAYSURF.blit(b_imgs[building.type], relativeCoordsToPixels(building.pos))
    highlight(autel1.pos,autel1.size)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
