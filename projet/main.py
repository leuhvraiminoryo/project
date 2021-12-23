from data.code.utils import *

orb1 = cl.Building('orb','standard',(-3,-2),(2,2))
orb1.lvl = 0
armurerie1 = cl.Building('armurerie','standard',(-5,3),(3,2))
armurerie1.lvl = 0
autel1 = cl.Building('autel','standard',(0,0),(2,2))
autel1.lvl = 0

list_buildings = [armurerie1,orb1,autel1]
placing = None
click = False
while True:
    checkForQuit()
    DISPLAYSURF.fill(BGCOLOR)
    text.show_text(str(e.ressources['soul_points']) + ' sp',2,10,1,9999,small_font,DISPLAYSURF)
    #text.show_text('Ceci est un petit test ... \\/:;,',160,50,5,99999,other_font,DISPLAYSURF)
    #e.ressources['soul_points'] += 1
    mouse_pos = pygame.mouse.get_pos ()
    
    to_highlight = None
    to_red = []
    to_menu = None

    if placing is not None:
        toPlace(placing,mouse_pos)

    placing = None

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            click = True
        elif event.type == MOUSEBUTTONUP:
            click = False

    for building in list_buildings:
        if building.lvl >= 0:
            building.update()
            blitBuilding(building)
            if mouseOverBuilding(building,mouse_pos):
                to_highlight = building
                if click:
                    to_menu = building
            if placing is not None:
                if buildingOverBuilding(placing,building):
                    to_red.append(building)
        else:
            placing = building

    if to_highlight is not None:
        if placing is None:
            highlight(to_highlight.pos,to_highlight.size)
    
    if to_red != list([]):
        blitBuilding(placing)
        for t_r in to_red:
            showTranspaRed(t_r)

    if to_menu is not None:
        drawMenu(to_menu)
    

    print(e.ressources)

    pygame.display.update()
    FPSCLOCK.tick(FPS)
