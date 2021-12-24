from data.code.utils import *

placing = None
left_click = False
right_click = False

list_buildings = load_buildings("projet/data/json/yeet.json")
print(list_buildings)

while True:
    checkForQuit(list_buildings)
    DISPLAYSURF.fill(BGCOLOR)
    text.show_text(str(e.ressources['soul_points']) + ' sp',2,10,1,9999,small_font,DISPLAYSURF)
    #text.show_text('Ceci est un petit test ... \\/:;,',160,50,5,99999,other_font,DISPLAYSURF)
    e.ressources['soul_points'] += 1
    mouse_pos = pygame.mouse.get_pos ()
    
    to_highlight = None
    to_red = []
    to_menu = None

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
            if event.button == 3:
                right_click = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            if event.button == 3:
                right_click = False

    if left_click:
        placing = None
    if placing is not None:
        toPlace(placing,mouse_pos)
        
    

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

    pygame.display.update()
    FPSCLOCK.tick(FPS)
