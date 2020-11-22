import pygame
import constants


class Snake:
    color = constants.SNAKE_COLOR

    def __init__(self, screen):
        self.screen = screen

        # give the snake an initial direction and body
        self.body = [
            (constants.COLUMNS // 4, constants.ROWS // 4),
            (constants.COLUMNS // 4, constants.ROWS // 4),
        ]
        self.direction = (1, 0)

    def check_movement_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not self.direction[1] == 1:
                self.direction = (0, -1)
            elif event.key == pygame.K_DOWN and not self.direction[1] == -1:
                self.direction = (0, 1)
            elif event.key == pygame.K_RIGHT and not self.direction[0] == -1:
                self.direction = (1, 0)
            elif event.key == pygame.K_LEFT and not self.direction[0] == 1:
                self.direction = (-1, 0)

    def move(self):
        head_x, head_y = self.body[0][0], self.body[0][1]
        new_head = head_x + self.direction[0], head_y + self.direction[1]
        self.body = [new_head] + self.body[:-1]

    def draw(self):
        for x, y in self.body:
            x *= constants.CUBE_WIDTH
            y *= constants.CUBE_HEIGHT
            square = pygame.Rect((x, y), (constants.CUBE_WIDTH, constants.CUBE_HEIGHT))
            pygame.draw.rect(self.screen, Snake.color, square)

    def is_dead(self):
        head_x, head_y = self.body[0]
        return (
            head_x in (-1, constants.COLUMNS)
            or head_y in (-1, constants.ROWS)
            or self.body[0] in self.body[1:]
        )

    def ate_food(self, food):
        return self.body[0] == food.position

    def increment_size(self):
        self.body.append(self.body[-1])
