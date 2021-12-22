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
"ic" : "qtt_ressources", "ec" : "max_equipement"}

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
        effect = effect.split()
        cd = effect[0]
        if cd == "n" and building.add_perm:
            building.add_perm = False
            ressources[codes[effect[1]]] += effect[2]
        if building.cooldowns[cd] >= effect[1]:
            ressources[codes[effect[2]]] += effect[3]
        
            

#for i in list_buildings:
#    data = json.dump(i, file, cls=CustomEncoder)
    

#res = extract('projet/dynamic_data/ressources.json')