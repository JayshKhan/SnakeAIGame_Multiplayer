from utils.config import Config
from ..algorithms.a_star import AStar
from ..algorithms.random import Random


class Snake:
    def __init__(self, name="default", driver="human", color=Config.DEFAULT_SNAKE_COLOR, canvas=None, food=None):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.name = name
        self.color = color
        self.canvas = canvas
        self.food = food
        self.eaten = True
        self.driver = driver  # human or astar, etc.


    def move(self):
        if self.driver == "human":
            pass
        elif self.driver == "astar":
            astar = AStar(self.snake, self.food)
            new_direction = astar.get_next_direction()
            if new_direction:
                self.direction = new_direction
        elif self.driver == "random":
            random_driver = Random()
            self.direction = random_driver.move(self.food.get_food_coords(), self.snake)
            print(f"directions from snake: {self.direction}")


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

    def paint_snake(self):
        self.canvas.delete(self.name)
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill=self.color,
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
