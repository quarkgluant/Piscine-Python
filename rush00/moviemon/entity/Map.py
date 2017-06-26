import random

class Map():
    def __init__(self, sizeX=10, sizeY=10):
        self.dataCase = {}
        if (sizeX < 10):
            self.sizeX = 10 
        else:
            self.sizeX = sizeX
        if (sizeY < 10):
            self.sizeY = 10
        else:
            self.sizeY = sizeY
        
        iX = 1
        iY = 1
        while iY <= sizeY:
            while iX <= sizeX:
                self.dataCase[str(iX) + ":" + str(iY)] = self.randomTypeCase()
                iX += 1
            iY += 1
            iX = 1
        
        randomValue = random.randint(0, len(self.dataCase))
        self.PlayerStart = list(self.dataCase.keys())[randomValue]

    def randomTypeCase(self):
        if random.random():
            return "movieball"
        else:
            return "moviemon"

    def getPlayerStart(self):
        split = self.PlayerStart.split(":")
        return {"x": split[0], "y": split[1]}