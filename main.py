import pygame, sys, os
from pygame.sprite import AbstractGroup
from pygame.math import Vector2


class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((920, 680))
        pygame.display.set_caption("PONG")
        self.icon = pygame.image.load('assets/ping-pong.png')
        pygame.display.set_icon(self.icon)
        self.middle_line = pygame.draw.line(self.screen, (255, 255, 255), (460,0),(460,680))

    def draw_player(self, color, x, y):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, 20, 105))
        pygame.display.update()

    def draw_ball(self, color, x, y):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, 20, 20))
        pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self, name, *groups: AbstractGroup):
        super().__init__(*groups)
        self.__name = name
        self.__points = 0
        self.color = (125, 125, 125)

    def add_points(self):
        self.__points += 1

    def get_points(self):
        return self.__points

    def get_name(self):
        return self.__name

    def update(self, pressed_key):
        if pressed_key[pygame.K_SPACE]:
            self.color = (45, 12, 200)
            pygame.display.flip()


class Ball:
    pass


class Game:
    def __init__(self):
        pygame.init()
        screen = Board()
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        screen.draw_player(player1.color, 50, 50)
        screen.draw_player(player2.color, 650, 250)
        screen.draw_ball((125, 150, 145), 250, 250)
        # player1 = Player(input("Player 2 - enter Your name: "))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

            pressed_key = pygame.key.get_pressed()
            player1.update(pressed_key)


if __name__ == '__main__':
    Game()
