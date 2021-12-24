import pygame, sys, json, data.code.extract
from pygame.locals import *
import data.code.classes as cl
import data.code.text as text
import data.code.extract as e
from data.code.extract import extract

#colors
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
ARED     = pygame.Color(255,   0,   0, a=50)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

#images
b_imgs = {
    'autel' : pygame.image.load('projet/data/images/autel.png'),
    'orb' : pygame.image.load('projet/data/images/orb.png'),
    #'residence' : pygame.image.load('projet/data/images/residence.png'),
    #'entrepot' : pygame.image.load('projet/data/images/entrepot.png'),
    'armurerie' : pygame.image.load('projet/data/images/armurerie.png'),
    #'decoration' : pygame.image.load('projet/data/images/decoration.png')
}

#setup
FPS = 20
BOXSIZE = 32
WX = BOXSIZE*20
WY = BOXSIZE*20
CAPTION = 'Préparez-vous à entrer dans Xak Tsaroth!!!'
FPSCLOCK = pygame.time.Clock()

BGCOLOR = GRAY
pygame.display.set_caption(CAPTION)
DISPLAYSURF = pygame.display.set_mode((WX,WY))

MENUX = 32
MENUY = 32

#setup buildings
orb1 = cl.Building('orb','standard',(-3,-2),(2,2))
orb1.lvl = 0
armurerie1 = cl.Building('armurerie','standard',(-5,3),(3,2))
armurerie1.lvl = 0
autel1 = cl.Building('autel','standard',(0,0),(2,2))
autel1.lvl = 0

list_buildings = [armurerie1,orb1,autel1]

# Text ------------------------------------------------------- #
def get_text_width(text,spacing,font_dat):
    width = 0
    for char in text:
        if char in font_dat:
            width += font_dat[char][0] + spacing
        elif char == ' ':
            width += font_dat['A'][0] + spacing
    return width

small_font_dat = {'A':[3],'B':[3],'C':[3],'D':[3],'E':[3],'F':[3],'G':[3],'H':[3],'I':[3],'J':[3],'K':[3],'L':[3],'M':[5],'N':[3],'O':[3],'P':[3],'Q':[3],'R':[3],'S':[3],'T':[3],'U':[3],'V':[3],'W':[5],'X':[3],'Y':[3],'Z':[3],
          'a':[3],'b':[3],'c':[3],'d':[3],'e':[3],'f':[3],'g':[3],'h':[3],'i':[1],'j':[2],'k':[3],'l':[3],'m':[5],'n':[3],'o':[3],'p':[3],'q':[3],'r':[2],'s':[3],'t':[3],'u':[3],'v':[3],'w':[5],'x':[3],'y':[3],'z':[3],
          '.':[1],'-':[3],',':[2],':':[1],'+':[3],'\'':[1],'!':[1],'?':[3],
          '0':[3],'1':[3],'2':[3],'3':[3],'4':[3],'5':[3],'6':[3],'7':[3],'8':[3],'9':[3],
          '(':[2],')':[2],'/':[3],'_':[5],'=':[3],'\\':[3],'[':[2],']':[2],'*':[3],'"':[3],'<':[3],'>':[3],';':[1]}
small_font = text.generate_font('projet/data/font/small_font.png',small_font_dat,5,8,(248,248,248))

other_font_dat = {'A':[3],'B':[3],'C':[3],'D':[3],'E':[3],'F':[3],'G':[3],'H':[3],'I':[3],'J':[3],'K':[3],'L':[3],'M':[5],'N':[3],'O':[3],'P':[3],'Q':[3],'R':[3],'S':[3],'T':[3],'U':[3],'V':[3],'W':[5],'X':[3],'Y':[3],'Z':[3],
          'a':[3],'b':[3],'c':[3],'d':[3],'e':[3],'f':[3],'g':[3],'h':[3],'i':[1],'j':[2],'k':[3],'l':[3],'m':[5],'n':[3],'o':[3],'p':[3],'q':[3],'r':[2],'s':[3],'t':[3],'u':[3],'v':[3],'w':[5],'x':[3],'y':[3],'z':[3],
          '.':[1],'-':[3],',':[2],':':[1],'+':[3],'\'':[1],'!':[1],'?':[3],
          '0':[3],'1':[3],'2':[3],'3':[3],'4':[3],'5':[3],'6':[3],'7':[3],'8':[3],'9':[3],
          '(':[2],')':[2],'/':[3],'_':[5],'=':[3],'\\':[3],'[':[2],']':[2],'*':[3],'"':[3],'<':[3],'>':[3],';':[1]}

other_font = text.generate_font('projet/data/font/new_font.png',other_font_dat,8,10,(248,248,248))


def relativeCoordsToPixels(coords,cor_x=(WX/2),cor_y=(WY/2)):
    x,y = coords
    return [(x*BOXSIZE)+cor_x,(y*BOXSIZE)+cor_y]

def pixelsToRelativeCoords(coords,cor_x=(WX/2),cor_y=(WY/2)):
    x,y = coords
    return [round((x-cor_x)/BOXSIZE),round((y-cor_y)/BOXSIZE)]

def terminateGame(l_b,res):
    save_buildings(l_b,"projet/data/json/yeet.json")
    save_res(res,"projet/data/json/ressources.json")
    pygame.quit()
    sys.exit()

def checkForQuit(l_b,res):
    for event in pygame.event.get(QUIT):
        terminateGame(l_b,res)
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminateGame(l_b,res)
        pygame.event.post(event)

def getBuildRect(pos,size,cor_pos=-1,cor_size=2,cor_r_pos_x=WX/2,cor_r_pos_y=WY/2):
    x,y = relativeCoordsToPixels(pos,cor_r_pos_x,cor_r_pos_y)
    sizex, sizey = size[0]*BOXSIZE,size[1]*BOXSIZE
    rect = pygame.Rect(x+cor_pos,y+cor_pos,sizex+cor_size,sizey+cor_size)
    return rect

def blitBuilding(building,fade=0):
    img = b_imgs[building.name]
    DISPLAYSURF.blit(img, relativeCoordsToPixels(building.pos))

def highlight(pos,size,color=WHITE):
    """Trace rectangle autours d'un buildet
    pos relative en boites
    size relative en boites"""
    rect = getBuildRect(pos,size)
    pygame.draw.rect(DISPLAYSURF, color, rect, width=1)

def mouseOverBuilding(building,mouse_pos):
    rect = getBuildRect(building.pos,building.size,0,0)
    if rect.collidepoint(mouse_pos):
        return True
    return False

def buildingOverBuilding(building1,building2):
    rect1 = getBuildRect(building1.pos,building1.size,0,0)
    rect2 = getBuildRect(building2.pos,building2.size,0,0)
    if rect1.colliderect(rect2):
        return True
    return False

def showTranspaRed(building):
    size = relativeCoordsToPixels(building.size,0,0)
    s = pygame.Surface(size)
    s.set_alpha(150)
    s.fill(RED)
    DISPLAYSURF.blit(s,relativeCoordsToPixels(building.pos))
    highlight(building.pos,building.size,BLACK)

def drawGrid():
    for x in range(0, WX, BOXSIZE):
        for y in range(0, WY, BOXSIZE):
            rect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)

def toPlace(building,mouse_pos):
    drawGrid()
    sizex,sizey = building.size
    building.pos = pixelsToRelativeCoords(mouse_pos,WX/2+(BOXSIZE*sizex/2),WY/2+(BOXSIZE*sizey/2))
    blitBuilding(building)
    


def isBuildRight(building):
    """check si le building selectioné est sur la droite relative de la fenêtre"""
    x,y = relativeCoordsToPixels(building.pos)
    if x > WX/2:
        return False
    return True
    
def getMenuCoords(building):
    x,y = relativeCoordsToPixels(building.pos)
    if isBuildRight(building):
        x += building.size[0] + 1
    else:
        x -= getMenuSize(building) - 1
    return (x,y)

def getListManips(building):
    """permet d'obtenir une liste de manipulations possibles sur un batiment selon son type par un fichier json"""
    return [1,2,3,4,5] #à modifier, liste temporaire pour tester les autres fonctions

def getMenuSize(building):
    nb_manips = len(getListManips(building))
    return MENUX * nb_manips

def cadreMenu(building):
    topL = getMenuCoords(building)
    x = getMenuSize(building)
    cadre = Rect(topL[0],topL[1],x,32)
    return cadre

def drawMenu(building):
    """fonction pour draw le menu de sélection d'un building"""
    size = getMenuSize(building)
    menu = pygame.Surface((size+10,MENUY)) #utiliser getMenuSize() fait bugguer?
    menu.fill(PURPLE)
    display_coords = relativeCoordsToPixels(building.pos)
    build_size = (building.size[0]*BOXSIZE,building.size[1]*BOXSIZE) 
    print(display_coords)
    display_coords[0] -= (size+10-build_size[0])/2
    display_coords[1] -= build_size[1] - MENUY-1
    print(display_coords)
    DISPLAYSURF.blit(menu,display_coords)
    

def save_buildings(list_buildings,file_name):
    dict_prin = {}
    for i in list_buildings:
        dict_prin[i.get_bat_id()] = i.tojson()
    with open(file_name,"w") as file:
        data = json.dump(dict_prin, file, cls=cl.CustomEncoder, sort_keys=True, indent=4)

def save_res(res,file_name):
    with open(file_name,"w") as file:
        data = json.dump(res,file)

def load_buildings(file):
    list_builds = []
    dict_prin = extract(file)
    for v in dict_prin.values():
        build = cl.Building(v["name"], v["type"],v["pos"],v["size"])
        build.id = v["id"]
        build.add_perm = v["add_perm"]
        build.cooldowns = v["cooldowns"]
        build.lvl = v["lvl"]
        list_builds.append(build)
    return list_builds




    
