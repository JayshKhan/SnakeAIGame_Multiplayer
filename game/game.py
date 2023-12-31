import os
import sys

from ui.base import BaseLayout
from utils.config import Config
from .components.food import Food
from .components.obstacle import get_obstacles
from .components.score_board import ScoreBoard
from .components.snake import Snake


class Game(BaseLayout):
    def __init__(self, master, no_of_snakes=1, ai="astar"):
        super().__init__(master)

        self.snakes = []
        self.no_of_snakes = no_of_snakes
        self.ai_algorithm = ai
        self.food = Food(self.canvas)
        self.obstacles, self.obstacles_coords = get_obstacles(self.canvas)

        self.score_board = ScoreBoard(no_of_snakes)
        self.set_snakes()
        self.master.bind("<KeyPress>", self.change_direction)
        self.game_time = 100
        self.game_ended = False
        self.update_time()
        self.update()

    def update_time(self):
        if self.game_time > 0:
            self.game_time -= 1
            self.canvas.delete("time")
            self.canvas.create_text(0 + 50,
                                    0,
                                    anchor="n", text=f"Time: {self.game_time}", font=("Arial", 12),
                                    fill="white", tag="time")
            self.master.after(1000, self.update_time)
        else:
            print("Time Over")
            self.game_over()
            return True

    def set_snakes(self):
        if self.no_of_snakes > 1:
            # first is human
            self.snakes.append(Snake(canvas=self.canvas, food=self.food,obstacles=self.obstacles_coords))
            remaining = self.no_of_snakes - 1
            for i in range(remaining):
                self.snakes.append(
                    Snake(driver=self.ai_algorithm, color=Config.OTHER_SNAKE_COLORS[i + 1], canvas=self.canvas,
                          food=self.food, obstacles=self.obstacles_coords))

        else:
            self.snakes.append(Snake(canvas=self.canvas, food=self.food,obstacles=self.obstacles_coords))

    def update(self):
        if not self.game_ended:
            food_coords = self.food.get_food_coords()
            for snake in self.snakes:
                # print(snake.get_snake(),food_coords,self.obstacles)
                snake.move(snake.get_snake(), food=food_coords)
                head = snake.get_snake()[0]
                snake.paint_snake()
                if snake.get_driver() == "human":
                    if self.check_game_over(head):
                        return

                if head[0] == food_coords[0] and head[1] == food_coords[1]:
                    snake.get_snake().append((0, 0))
                    for sna in self.snakes:
                        print(f"setting path empty for {sna.get_name()}")
                        sna.path = []
                    self.canvas.delete("food")
                    self.food.paint(self.canvas)
                    snake.set_score(snake.get_score() + 1)
            self.score_board.update_scoreboard(self.snakes[0].get_score(),
                                               self.snakes[1].get_score() if self.no_of_snakes > 1 else None)

            self.master.after(200, self.update)

    def change_direction(self, event):
        if event.keysym == "Right" and not self.snakes[0].get_direction() == "Left":
            self.snakes[0].set_direction("Right")
        elif event.keysym == "Left" and not self.snakes[0].get_direction() == "Right":
            self.snakes[0].set_direction("Left")
        elif event.keysym == "Up" and not self.snakes[0].get_direction() == "Down":
            self.snakes[0].set_direction("Up")
        elif event.keysym == "Down" and not self.snakes[0].get_direction() == "Up":
            self.snakes[0].set_direction("Down")

    def check_game_over(self, head):
        if head[0] < 0 or head[0] > Config.SCREEN_WIDTH - 20 or head[1] < 0 or head[1] > Config.SCREEN_HEIGHT - 20:
            print("Touched Border")
            self.game_over()
            return True

        # # check if the snake hits itself
        for segment in self.snakes[0].get_snake()[1:]:
            if head[0] == segment[0] and head[1] == segment[1]:
                print("Touched Itself")
                self.game_over()
                return True
        #
        # # check if the snake hits the obstacle
        for obstacle in self.obstacles:
            obstacle_coords = self.obstacles_coords
            if head[0] == obstacle_coords[0] and head[1] == obstacle_coords[1]:
                print("Touched Obstacle")
                self.game_over()
                return True

        return False

    def game_over(self):
        self.game_ended = True
        if self.no_of_snakes > 1:
            score1 = self.snakes[0].get_score()
            score2 = self.snakes[1].get_score()
        else:
            score1 = self.snakes[0].get_score()
            score2 = None
        for snake in self.snakes:
            self.snakes.remove(snake)

        self.canvas.delete("time")
        self.game_time = 0
        self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                Config.SCREEN_HEIGHT / 2,
                                anchor="center", text="Game Over", font=("Arial", 30), fill="white")
        # declare the winner
        if score2 is not None:
            if score1 > score2:
                self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                        Config.SCREEN_HEIGHT / 2 + 50,
                                        anchor="center", text="Player 1 Wins", font=("Arial", 20), fill="white")
            elif score1 < score2:
                self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                        Config.SCREEN_HEIGHT / 2 + 50,
                                        anchor="center", text="Player 2 Wins", font=("Arial", 20), fill="white")
            else:
                self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                        Config.SCREEN_HEIGHT / 2 + 50,
                                        anchor="center", text="Draw", font=("Arial", 20), fill="white")

        else:
            self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                    Config.SCREEN_HEIGHT / 2 + 50,
                                    anchor="center", text="You Lost with Score: " + str(score1), font=("Arial", 20),
                                    fill="white")

        self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                Config.SCREEN_HEIGHT / 2 + 100,
                                anchor="center", text="Press Space to Restart", font=("Arial", 20), fill="white")
        self.master.bind("<space>", self.restart)

    def restart(self, event):
        self.master.destroy()
        # delete everything and retart from the main.py
        os.execl(sys.executable, sys.executable, *sys.argv)
