import json

class Building:
    def __init__(self, id, type):
        self.id = id
        self.type = type
    def affichage(self):
        print(self.type)
    def tojson(self):
        return {
            "id" : self.id,
            "type": self.type
        }
    

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if "tojson" in dir(o):
            return o.tojson()
        return json.JSONEncoder.default(self, o)

a = Building('Orb1', 'orb')

list_buildings = [a]
