import json


dict = {}

while True:
    entry = input()
    if entry == 'n':
        break
    dict.setdefault(entry,{"price" : 0, "quantity" : 0, "upgradable" : True})
    print(dict.items())

file = open("projet/buildings.json", "w")
json.dump(dict, file)