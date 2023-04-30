import pygame
from gameSettings import *
from tileset import Tileset
from tileset import Victory
from mainChar import PlayerChar

class GameWorld:
    def __init__(self):
        #delcaring object groups
        self.displaySurface = pygame.display.get_surface()
        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.winSprites = pygame.sprite.Group()

        self.generateMap()

    def generateMap(self):
        #calls object group by calling class and giving it a key to be placed on the map
        for row_index, row in enumerate(World_Map):
            for col_index, col in enumerate(row):
                x = col_index * Tilesize
                y = row_index * Tilesize
                if col == "w":
                    Tileset((x,y), [self.visibleSprites, self.obstacleSprites])
                if col == "p":
                    PlayerChar((x,y), [self.visibleSprites], self.obstacleSprites, self.winSprites)

                if col == "x":
                    Victory((x, y), [self.visibleSprites, self.winSprites])


    def draw(self):
        #draws objects
        self.visibleSprites.draw(self.displaySurface)
        self.visibleSprites.update()

        pass
