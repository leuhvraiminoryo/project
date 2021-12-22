import json
from classes import *

#fonction d'extraction de fichier json :
def extract(file : str):
    with open(file) as j_file:
        dict = json.load(j_file)
    return dict

#extraction du fichier de propriétés des batiments :
tree = extract("projet/data/json/build_properties.json")

#répartition des différents arbres d'évolution :
orb_tree = tree["orb"]
autel_tree = tree["autel"]
armurerie_tree = tree["armurerie"]
residences_tree = tree["residences"]
entrepot_tree = tree["entrepot"]

#liste des décorations :
decorations = tree["decorations"]

def decodage(building):
    code = tree[building.name][building.type][building.level].split('; ')
    for effect in code:
        if code.startswith("n"):

        











#for i in list_buildings:
#    data = json.dump(i, file, cls=CustomEncoder)
    

#res = extract('projet/dynamic_data/ressources.json')
