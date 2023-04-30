import pygame
from gameSettings import *
pygame.font.init()

screen = pygame.display.set_mode((Width, Height))
playerSpriteSheet = pygame.image.load("Assets/Sprites/Wizard/Wizard_Blue1.png").convert_alpha()
font30 = pygame.font.Font(None, 90)


def getImage(sheet, w, h):
    # gets sprite image from a specific coordinate of pixels
    image = pygame.Surface((w, h)).convert_alpha()
    image.blit(sheet, (0, 0), (8, 6, w, h))


    return image

#creating player
class PlayerChar(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites, winSprites):
        # gives player
        super().__init__(groups)
        self.image = self.image = getImage(playerSpriteSheet, 16, 16)
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.obstacleSprites = obstacleSprites
        self.winSprites = winSprites


    def input (self): # controls
        controls = pygame.key.get_pressed()

        if controls [pygame.K_UP]:
            self.direction.y = -1
        elif controls [pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if controls[pygame.K_RIGHT]:
            self.direction.x = 1
        elif controls[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def movement(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # makes sure that the player doesn't move faster when moving diagonally

        self.rect.x += self.direction.x * speed
        self.playerCollision("h")
        self.rect.y += self.direction.y * speed
        self.playerCollision("v")

    def playerCollision(self, direction): #collsions
        gameWinner = False
        if direction == "h": #horizontal collisions
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = self.rect.right
            for sprite in self.winSprites:
                if sprite.rect.colliderect(self.rect):
                    gameWinner = True

        if direction == "v": #vertical collisions
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = self.rect.bottom
            for sprite in self.winSprites:
                if sprite.rect.colliderect(self.rect):
                    gameWinner = True

        if gameWinner == True:
            screen.blit(font30.render('YOU WIN!', True, (255, 255, 255)), (500, 320))


    def update(self):
        self.input()
        self.movement(self.speed)

