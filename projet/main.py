from data.code.utils import *

orb1 = cl.Building('orb',(-1,1),(1,1))
orb1.lvl = 0
armurerie1 = cl.Building('armurerie',(-5,3),(3,2))
armurerie1.lvl = -1
autel1 = cl.Building('autel',(0,0),(2,2))
autel1.lvl = 0

list_buildings = [armurerie1,orb1,autel1]
placing = None
click = False
while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    mouse_pos = pygame.mouse.get_pos ()
    
    to_highlight = None
    to_red = []

    if placing is not None:
        toPlace(placing,mouse_pos)

    placing = None

    for building in list_buildings:
        if building.lvl >= 0:
            blitBuilding(building)
            if mouseOverBuilding(building,mouse_pos):
                to_highlight = building
                for event in pygame.event.get(KEYUP):
                    if event.type == MOUSEBUTTONDOWN:
                        click = True
                    elif event.type == MOUSEBUTTONUP:
                        click = False
            if buildingOverBuilding(placing,building):
                to_red.append(building)
        else:
            placing = building
    
    for event in pygame.event.get(KEYUP):
        if event.type == MOUSEBUTTONDOWN:
            click = True
        elif event.type == MOUSEBUTTONUP:
            click = False
    
    if click:
        drawMenu()

    if to_highlight is not None:
        if placing is None:
            highlight(to_highlight.pos,to_highlight.size)
    
    if to_red != list([]):
        blitBuilding(placing)
        for t_r in to_red:
            showTranspaRed(t_r)
    


    pygame.display.update()
    FPSCLOCK.tick(FPS)
