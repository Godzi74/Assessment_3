import pygame
from gameSettings import *
from tileset import Tileset

class GameWorld:
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()
        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.interactableSprites = pygame.sprite.Group()

        self.generateMap()

    def generateMap(self):
        for row_index, row in enumerate(World_Map):
            for col_index, col in enumerate(row):
                x = col_index * Tilesize
                y = row_index * Tilesize
                if col == "w":
                    Tileset((x,y), [self.visibleSprites])

    def draw(self):
        self.visibleSprites.draw(self.displaySurface)

        pass
