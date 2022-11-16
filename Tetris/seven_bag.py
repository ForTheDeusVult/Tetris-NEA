import random

class bag:

    def __init__ (self):
        self._7bag = [0, 1, 2, 3, 4, 5, 6]
        self._count=-1

    def __shuffle__(self):
        self._shuffle = random.shuffle(self._7bag)

    def increment(self):
        self._count+=1
        if self._count == 7:
            self.__shuffle__()
        return(self._7bag)