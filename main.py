import pygame, sys
from gameSettings import *
from gameWorld import GameWorld

class MainGame:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        self.timer = pygame.time.Clock()
        pygame.display.set_caption("Split Hero")

        self.gameWorld = GameWorld()
    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.gameWorld.draw() # calls gameWorld method
            pygame.display.update()
            self.timer.tick(FPS)


if __name__ == "__main__":
    game = MainGame()
    game.runGame()
