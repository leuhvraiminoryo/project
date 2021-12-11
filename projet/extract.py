import json, classes
from classes import *

def extract(file : str):
    with open(file) as j_file:
        dict = json.load(j_file)
    return dict

file = open("projet/dynamic_data/test.json", "w")

for i in classes.list_buildings:
    data = json.dump(i, file, cls=CustomEncoder)
    

#res = extract('projet/dynamic_data/ressources.json')
