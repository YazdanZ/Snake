from random import randint
import pygame

import constants


class Food:
    color = constants.FOOD_COLOR

    def __init__(self, screen):
        self.screen = screen
        self.position = (
            randint(0, constants.ROWS - 1),
            randint(0, constants.COLUMNS - 1),
        )

    def generate_food(self, snake):
        new_position = None
        while new_position is None:
            row = randint(0, constants.ROWS - 1)
            column = randint(0, constants.COLUMNS - 1)
            if not (row, column) in snake.body:
                new_position = (row, column)
        self.position = new_position

    def draw(self):
        x = constants.CUBE_WIDTH * self.position[0]
        y = constants.CUBE_HEIGHT * self.position[1]
        square = pygame.Rect((x, y), (constants.CUBE_WIDTH, constants.CUBE_HEIGHT))
        pygame.draw.rect(self.screen, Food.color, square)
