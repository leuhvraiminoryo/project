from data.code.utils import *

autel1 = cl.Building('autel',(0,0),(2,2))
orb1 = cl.Building('orb',(-1,1),(1,1))

list_buildings = [autel1,orb1]

while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    mouse_pos = pygame.mouse.get_pos ()
    to_highlight = None
    
    for building in list_buildings:
        DISPLAYSURF.blit(b_imgs[building.type], relativeCoordsToPixels(building.pos))
        if mouseOverBuilding(building,mouse_pos):
            to_highlight = building
    
    if not to_highlight is None:
        highlight(to_highlight.pos,to_highlight.size)

    pygame.display.update()
    FPSCLOCK.tick(FPS)
