from moviemon.entity.Map import *
from moviemon.entity.Player import *
import pickle

class Game():

    def __init__(self):
        self.mapX = 10
        self.mapY = 20
        self.fileGame = "game.save"
        self.map = Map(self.mapX, self.mapY)

        playerStart = self.map.getPlayerStart()
        print("New Game : ", playerStart)
        self.player = Player(1, 10, playerStart.get("x"), playerStart.get("y") )
    
    def load(self):
        pass
    
    def dump(self):
        pass

    def get_random_movie(self):
        pass
    
    def load_default_settings(self):
        pass
    
    def get_strength(self):
        pass

    def get_movie(self, id):
        pass
    
    def save_game(self):
        pickle.dump(self, open(self.fileGame, "wb" ) )
    
    def load_game(self):
        print("After load : ", self.map.getPlayerStart())
