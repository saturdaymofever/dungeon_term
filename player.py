import random, constant

class Player:
    coord = None
    pv = None
    pw = None

    def __init__(self, pv=constant.INITIAL_PV, pw=constant.INITIAL_PW):
        self.pw = pw
        self.pv = pv
        self.move()

    def takehit(self):
        self.pv -= 1

    def uppower(self):
        self.pw += 1

    def move(self):
        self.coord = (random.randint(1,constant.mapV),random.randint(1,constant.mapH))








