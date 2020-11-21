import pygame, sys, random
from enum import Enum

import constants
import time
from food import Food
from snake import Snake


class Directions(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Game:
    def __init__(self):
        self.start_game()

    def start_game(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.set_screen()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.game_loop()

    def game_loop(self):
        while True:
            # 10 frame per second
            self.clock.tick(15)
            self.check_events()
            self.snake.move()
            if self.snake.is_dead():
                break
            self.update_screen()

    def set_screen(self):
        self.screen = pygame.display.set_mode(constants.SCREEN_DIMENSIONS)
        pygame.display.set_caption("IntelliSnake")
        pygame.mouse.set_visible(False)

    def update_screen(self):
        self.screen.fill(constants.BG_COLOR)
        self.snake.draw()
        self.food.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            Game.check_exit_event(event)
            self.snake.check_movement_events(event)

    @staticmethod
    def check_exit_event(event):
        if event.type == pygame.QUIT:
            sys.exit()


Game()
