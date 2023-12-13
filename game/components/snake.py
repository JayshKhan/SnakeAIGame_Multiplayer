import random

from utils.config import Config


class Snake:
    def __init__(self, name="default", driver="human", color=Config.DEFAULT_SNAKE_COLOR):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.name = name
        self.color = color
        self.driver = driver  # human or astar, etc.

    def move(self):
        if self.driver == "human":
            new_head = None
            head = self.snake[0]
            if self.direction == "Right":
                new_head = (head[0] + 20, head[1])
            elif self.direction == "Left":
                new_head = (head[0] - 20, head[1])
            elif self.direction == "Up":
                new_head = (head[0], head[1] - 20)
            elif self.direction == "Down":
                new_head = (head[0], head[1] + 20)

            self.snake.insert(0, new_head)
            self.snake.pop()
        elif self.driver == "astar":
            # AStar Algorithm
            pass
        elif self.driver == "random":
            directions = ["Up", "Down", "Left", "Right"]
            self.enemy_direction = random.choice(directions)
            head = self.snake[0]
            if self.enemy_direction == "Right":
                new_head = (head[0] + 20, head[1])
            elif self.enemy_direction == "Left":
                new_head = (head[0] - 20, head[1])
            elif self.enemy_direction == "Up":
                new_head = (head[0], head[1] - 20)
            elif self.enemy_direction == "Down":
                new_head = (head[0], head[1] + 20)

            self.snake.insert(0, new_head)
            self.snake.pop()

    def paint_snake(self, canvas):
        canvas.delete(self.name)
        for segment in self.snake:
            canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill=self.color,
                                    tags=self.name)

    # getters
    def get_snake(self):
        return self.snake

    def get_direction(self):
        return self.direction

    def get_name(self):
        return self.name

    def get_driver(self):
        return self.driver

    def set_direction(self, direction):
        self.direction = direction
