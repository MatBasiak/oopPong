import pygame, sys, os


class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 480))
        pygame.display.set_caption("PONG")
        self.icon = pygame.image.load('assets/ping-pong.png')
        pygame.display.set_icon(self.icon)


class Player():
    def __init__(self, name):

        self.__name = name
        self.__points = 0
        self.rect =

    def add_points(self):
        self.__points += 1

    def get_points(self):
        return self.__points

    def get_name(self):
        return self.__name

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            pass


class Ball:
    pass


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        # player1 = Player("Player 1", self.screen)
        # player1 = Player(input("Player 2 - enter Your name: "))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)


if __name__ == '__main__':
    Game()
