from django.shortcuts import render
from moviemon.entity.Game import *

myGame = Game()

def worldMap(request, param = None):
    title = "worldmap"

    if param == "up":
        myGame.player.moveUp()
    elif param == "down":
         myGame.player.moveDown()
    elif param == "left":
         myGame.player.moveLeft()
    elif param == "right":
         myGame.player.moveRight()
    elif param == "a":
         myGame.player.moveRight()

    return render(request, 'moviemon/worldmap.html', {
        "title": title,
        "columns": range(1, myGame.mapX),
        "rows": range(1, myGame.mapY),
        "player_col": myGame.player.posX,
        "player_row": myGame.player.posY
    })
    
