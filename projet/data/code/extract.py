import json

#fonction d'extraction de fichier json :
def extract(file : str):
    with open(file) as j_file:
        dict = json.load(j_file)
    return dict

#extraction du fichier de propriétés des batiments et de ressources :
tree = extract("projet/data/json/build_properties.json")
ressources = extract("projet/data/json/ressources.json")
codes = {"sp" : "soul_points", 
"f" : "faith", "ae" : "aesthetic", 
"h" : "happiness", "r" : "residents", 
"fc" : "max_faith", "spc" : "max_sp", 
"ic" : "qtt_ressources", "ec" : "max_equipement",
"rc" : "max_residents"}

#répartition des différents arbres d'évolution :
orb_tree = tree["orb"]
autel_tree = tree["autel"]
armurerie_tree = tree["armurerie"]
residence_tree = tree["residence"]
entrepot_tree = tree["entrepot"]

#liste des décorations :
decorations = tree["decoration"]

def decodage(building):
    code = tree[building.category][building.type][building.lvl].split('; ')
    for effect in code:
        effect = effect.split()
        cd = effect[0]
        if cd == "n" and building.add_perm:
            building.add_perm = False
            ressources[codes[effect[2]]] += int(effect[3])
        elif building.cooldowns[cd] >= int(effect[1]):
            building.cooldowns[cd] = 0
            ressources[codes[effect[2]]] += int(effect[3])
        
#res = extract('projet/dynamic_data/ressources.json')

buildsize = extract("projet/data/json/builds_sizes.json")