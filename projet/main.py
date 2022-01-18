from data.code.utils import *

placing = None
left_click = False
right_click = False



pressed = {
        "a" : False,
        "r" : False,
        "o" : False,
        "d" : False,
        "e" : False,
        "w" : False,
        "del" : False
    }


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
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
            if event.button == 3:
                right_click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            if event.button == 3:
                right_click = False
        pygame.event.post(event)
            


    for event in pygame.event.get(KEYUP):
        if event.key == K_a:
            pressed["a"] = False
        if event.key == K_e:
            pressed["e"] = False
        if event.key == K_w:
            pressed["w"] = False
        if event.key == K_o:
            pressed["o"] = False
        if event.key == K_d:
            pressed["d"] = False
        if event.key == K_r:
            pressed["r"] = False
        if event.key == K_BACKSPACE:
            pressed["del"] = False
    
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_a:
            pressed["a"] = True
        if event.key == K_e:
            pressed["e"] = True
        if event.key == K_w:
            pressed["w"] = True
        if event.key == K_o:
            pressed["o"] = True
        if event.key == K_d:
            pressed["d"] = True
        if event.key == K_r:
            pressed["r"] = True
        if event.key == K_BACKSPACE:
            pressed["del"] = True
    

    if left_click:
        placing = None
    if placing is not None:
        toPlace(placing,mouse_pos)
    if True in pressed.values():
        print('detected')
        for building in list_buildings:
            if buildingOverBuilding(pixelsToBoxCoords(mouse_pos),(2,2),building) and pressed["del"]:
                list_buildings.pop(list_buildings.index(building))
            if buildingOverBuilding(pixelsToBoxCoords(mouse_pos),(2,2),building):
                posable = False

        if posable:
            if pressed["o"]:
                list_buildings.append(cl.Building('orb','standard',pixelsToBoxCoords(mouse_pos),(2,2)))
            if pressed["a"]:
                list_buildings.append(cl.Building('autel','standard',pixelsToBoxCoords(mouse_pos),(2,2)))
            if pressed["e"]:
                list_buildings.append(cl.Building('entrepot','standard',pixelsToBoxCoords(mouse_pos),(2,1)))
            if pressed["r"]:
                list_buildings.append(cl.Building('residence','standard',pixelsToBoxCoords(mouse_pos),(1,1)))
            if pressed["w"]:
                list_buildings.append(cl.Building('armurerie','standard',pixelsToBoxCoords(mouse_pos),(3,2)))
            if pressed["d"]:
                list_buildings.append(cl.Building('decoration','arbre',pixelsToBoxCoords(mouse_pos),(1,1)))

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
