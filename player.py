import random

class Player:

    pv = 10 #point de vie
    pw = 2 #power
    sh = 0 #Shield
    coord = (10,12)
    def takehit(self):
        self.pv -= 1
    def uppower(self):
        self.pw += 1
    def move(self, mapV, mapH):
        self.coord = (random.randint(1,mapV),random.randint(1,mapH))




player = Player()
player2 = Player()

player.takehit()
player.move(3,3)


print(player.coord)
