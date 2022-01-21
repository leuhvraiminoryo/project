from data.code.utils import *
    
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


def verif_keys(pressed,left_click,right_click):
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

    return pressed, left_click, right_click