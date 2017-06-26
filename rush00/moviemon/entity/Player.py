class Player():

    def __init__(self, power, movieBalls, posX, posY):
        self.power = power
        self.myMovieBalls = movieBalls
        self.myMovieMons = []
        self.posX = int(posX)
        self.posY = int(posY)
    
    def moveUp(self):
        self.posY += 1
        return self.posX

    def moveDown(self):
        self.posY -= 1
        return self.posX
    
    def moveRight(self):
        self.posX += 1
        return self.posY
    
    def moveLeft(self):
        self.posX -= 1
        return self.posX