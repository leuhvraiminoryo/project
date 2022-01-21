from data.code.utils import *
from data.code.keys_verif import *

placing = None

while True:
    checkForQuit(list_buildings,e.ressources)
    DISPLAYSURF.fill(BGCOLOR)
    text.show_text(str(e.ressources['soul_points']) + ' sp',2,10,1,9999,small_font,DISPLAYSURF)
    #text.show_text('Ceci est un petit test ... \\/:;,',160,50,5,99999,other_font,DISPLAYSURF)
    e.ressources['soul_points'] += 1
    mouse_pos = pygame.mouse.get_pos ()
    
    
    to_highlight = None
    to_red = []
    to_menu = None
    posable = True

    pressed,left_click,right_click = verif_keys(pressed,left_click,right_click)

    if left_click:
        placing = None
    if placing is not None:
        toPlace(placing,mouse_pos)

    if True in pressed.values():
        
        if pressed["o"]:
            a_poser = cl.Building('orb','standard',pixelsToBoxCoords(mouse_pos),(2,2))
        if pressed["a"]:
            a_poser = cl.Building('autel','standard',pixelsToBoxCoords(mouse_pos),(2,2))
        if pressed["e"]:
            a_poser = cl.Building('entrepot','standard',pixelsToBoxCoords(mouse_pos),(2,1))
        if pressed["r"]:
            a_poser = cl.Building('residence','standard',pixelsToBoxCoords(mouse_pos),(1,1))
        if pressed["w"]:
            a_poser = cl.Building('armurerie','standard',pixelsToBoxCoords(mouse_pos),(3,2))
        if pressed["d"]:
            a_poser = cl.Building('decoration','arbre',pixelsToBoxCoords(mouse_pos),(1,1))
        
        for building in list_buildings:
            if buildingOverBuilding(pixelsToBoxCoords(mouse_pos),(1,1),building) and pressed["del"]:
                list_buildings.pop(list_buildings.index(building))
            if buildingOverBuilding(pixelsToBoxCoords(mouse_pos),(e.buildsize[a_poser.category]["size_x"],e.buildsize[a_poser.category]["size_y"]),building):
                posable = False

        if posable:
            list_buildings.append(a_poser)


    for building in list_buildings:
        if building.lvl >= 0:
            building.update()
            blitBuilding(building)
            if mouseOverBuilding(building,mouse_pos):
                to_highlight = building
                #if right_click:
                #    to_menu = building
                if right_click:
                    placing = building
            if placing is not None:
                if buildingOverBuilding(placing.pos,placing.size,building):
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

    pygame.display.update()
    FPSCLOCK.tick(FPS)
