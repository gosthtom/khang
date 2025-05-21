import random

class Game:
    def __init__(self, type='xúc xắc'):
        self.type = type 
        self.score_list = [] 
    @property
    def score(self):
        if (self.type == 'đồng xu'):
            return random.randint(0, 1)
        elif (self.type == 'xúc xắc'):
            return random.randint(1, 6)
    @property
    def quantity(self):
        return len(self.score_list)

    @quantity.setter
    def quantity(self, new_quantity):
        for _ in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.score_list = [] 
        self.score_list = []