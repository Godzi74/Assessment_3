import pygame, sys
from pygame import mixer
from gameSettings import *
from gameWorld import GameWorld
pygame.font.init()
mixer.init()
music = pygame.mixer.Sound("Assets/dungeon_theme_2.mp3")
music.set_volume(0.1)
music.play(-1)
class MainGame:
    # main game frame
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        self.timer = pygame.time.Clock()
        pygame.display.set_caption("Maze man")



        self.gameWorld = GameWorld()


    def runGame(self):

        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)
        counter = 90
        font30 = pygame.font.Font(None, 30)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == timer_event:
                    counter -= 1
                    print(counter)

                if counter < 0:
                    pygame.quit
                    sys.exit()


            self.screen.fill("black")
            self.screen.blit(font30.render('Time: {}'.format(counter), True, (255, 255, 255)), (1070, 22))
            self.gameWorld.draw() # calls gameWorld method
            pygame.display.update()
            self.timer.tick()
            self.timer.tick(FPS)


if __name__ == "__main__":
    game = MainGame()
    game.runGame()
# runs game.