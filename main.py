import pygame, sys, os
from pygame.sprite import AbstractGroup


class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("PONG")
        self.icon = pygame.image.load('assets/ping-pong.png')
        pygame.display.set_icon(self.icon)
        self.middle_line = pygame.draw.line(self.screen, (255, 255, 255), (width / 2, 0), (width / 2, height))

    def draw_player(self, color, x, y):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, 20, 100))
        pygame.display.update()

    def draw_ball(self, color, x, y):
        pygame.draw.circle(self.screen, color, (x, y), 20, 20)
        pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self, name, color, position_x, position_y, *groups: AbstractGroup):
        super().__init__(*groups)
        self.__name = name
        self.__points = 0
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

    def add_points(self):
        self.__points += 1

    def get_points(self):
        return self.__points

    def get_name(self):
        return self.__name

    def update(self, pressed_key):
        if pressed_key[pygame.K_s]:
            self.position_y += 10
            pygame.display.update()


class Game:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self):
        pygame.init()
        screen = Board(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        player1 = Player("Player 1", (125, 124, 255), 10, 50)
        player2 = Player("Player 2", (255, 255, 255), Game.SCREEN_WIDTH - 30, Game.SCREEN_HEIGHT - 150)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            screen.draw_player(player1.color, player1.position_x, player1.position_y)
            screen.draw_player(player2.color, player2.position_x, player2.position_y)
            screen.draw_ball((125, 150, 145), Game.SCREEN_WIDTH / 2, Game.SCREEN_HEIGHT / 2)
            pressed_key = pygame.key.get_pressed()
            player1.update(pressed_key)


if __name__ == '__main__':
    Game()
