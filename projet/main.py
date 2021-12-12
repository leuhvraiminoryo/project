from data.code.utils import *

autel1 = cl.Building('autel',(0,0),(2,2))
autel1.lvl = 0
orb1 = cl.Building('orb',(-1,1),(1,1))

list_buildings = [autel1,orb1]
placing = None

while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    mouse_pos = pygame.mouse.get_pos ()
    to_highlight = None

    if placing is not None:
        toPlace(placing,mouse_pos)

    placing = None

    for building in list_buildings:
        if building.lvl >= 0:
            blitBuilding(building)
            if mouseOverBuilding(building,mouse_pos):
                to_highlight = building
        else:
            placing = building
    
    if to_highlight is not None:
        if placing is None:
            highlight(to_highlight.pos,to_highlight.size)
        else:
            showTranspaRed(to_highlight)

    pygame.display.update()
    FPSCLOCK.tick(FPS)
