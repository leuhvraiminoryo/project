import json

class Building:
    id = 0
    def __init__(self,type,pos,size):
        self.type = type
        self.id = Building.id
        Building.id += 1
        self.pos = pos
        self.lvl = -1
        self.size = size

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