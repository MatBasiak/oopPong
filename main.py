import pygame, sys


class Player:
    def __init__(self, name):
        super(Game, self).__init()
        self.__name = name
        self.__points = 0
        self.rect = pygame.draw.rect(Game.screen, (20, 50))

    def add_points(self):
        self.__points += 1

    def get_points(self):
        return self.__points

    def get_name(self):
        return self.__name

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            pass


class Board:
    def __init__(self):
        screen = pygame.display.set_mode((720, 480))
        pygame.display.set_caption("PONG")


class Game:
    screen = Board()
    # player1 = Player(input("Player 1 - enter Your name: "))
    # player1 = Player(input("Player 2 - enter Your name: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                sys.exit(0)


if __name__ == '__main__':
    Game()
