import json, time

from data.code.extract import decodage

class Building:
    id = 0
    def __init__(self,category,type,pos,size):
        self.category = category
        self.type = type
        self.id = Building.id
        Building.id += 1
        self.pos = pos
        self.lvl = 0
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
            "category" : self.category,
            "type" : self.type,
            "id" : self.id,
            "pos" : self.pos,
            "lvl" : self.lvl,
            "size" : self.size,
            "cooldowns" : self.cooldowns,
            "add_perm" : self.add_perm
        }
    def get_bat_id(self):
        return self.category + str(self.id)
    
    def lvlup(self):
        self.lvl += 1
    

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if "tojson" in dir(o):
            return o.tojson()
        return json.JSONEncoder.default(self, o)
