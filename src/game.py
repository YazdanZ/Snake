import pygame, sys, time, json, os

import constants
from food import Food
from snake import Snake


class Game:
    def __init__(self):
        self.start_game()

    def start_game(self):
        Game.create_scores_file()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.set_screen()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.game_loop()

    def game_loop(self):
        while True:
            # 15 frame per second
            self.clock.tick(15)
            self.check_events()
            self.snake.move()
            if self.snake.ate_food(self.food):
                self.snake.increment_size()
                self.food.generate_food(self.snake)
            if self.snake.is_dead():
                Game.update_stats(len(self.snake.body))
                Game.print_stats(len(self.snake.body))
                time.sleep(0.5)
                self.start_game()
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

    @staticmethod
    def create_scores_file():
        if not os.path.exists("stats.json"):
            stats = {"High Score": 0, "Games Played": 0}
            with open("stats.json", "w") as json_file:
                json.dump(stats, json_file)

    @staticmethod
    def update_stats(score):
        with open("stats.json", "r+") as json_file:
            stats = json.load(json_file)
            json_file.seek(0, 0)
            stats["Games Played"] = int(stats["Games Played"]) + 1
            if score > int(stats["High Score"]):
                stats["High Score"] = score
            json.dump(stats, json_file)

    @staticmethod
    def print_stats(score):
        with open("stats.json", "r") as json_file:
            stats = json.load(json_file)

        scoreboard = """
                        ---------------------------------
                        |             stats             |
                        ---------------------------------
                        ---------------------------------
                        score: {}                     
                        high score: {}                
                        games played: {}              
                        ---------------------------------""".format(
            score, stats["High Score"], stats["Games Played"]
        )

        _ = os.system("clear")
        print(scoreboard)


Game()
