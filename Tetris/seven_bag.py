import random

class bag:

    def __init__ (self):
        self._7bag = [0, 1, 2, 3, 4, 5, 6]

    def __shuffle__(self):
        self._7bag = random.shuffle(self._7bag)
        
