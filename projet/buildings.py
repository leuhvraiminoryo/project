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

