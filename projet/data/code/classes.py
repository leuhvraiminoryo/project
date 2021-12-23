import json, time

from data.code.extract import decodage

class Building:
    id = 0
    def __init__(self,name,type,pos,size):
        self.name = name
        self.type = type
        self.id = Building.id
        Building.id += 1
        self.pos = pos
        self.lvl = -1
        self.size = size
        self.cooldowns = {"n":-1,"tg" : 0, "trg" : 0, "rrg" : 0, "wrg" : 0}
        self.add_perm = True

    def update(self):
        self.cooldowns["tg"] += 0.1
        decodage(self)

    def print_data(self):
        print(self.type,self.lvl,self.pos)
        
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
