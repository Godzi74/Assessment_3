import pygame
from gameSettings import *

screen = pygame.display.set_mode((Width, Height))
tilesetSpriteSheet = pygame.image.load("Assets/Sprites/Tiles/FullTileset.png").convert_alpha()


def getImage(sheet, w, h):
    image = pygame.Surface((w, h)).convert_alpha()
    image.blit(sheet, (0, 0), (224, 48, w, h))

    return image


image1 = getImage(tilesetSpriteSheet, 16, 16)


class Tileset(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = getImage(tilesetSpriteSheet, 16, 16)
        self.rect = self.image.get_rect(topleft=pos)
