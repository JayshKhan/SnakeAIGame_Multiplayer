from utils.config import Config
from ..algorithms.a_star import AStar
from ..algorithms.greedy import Greedy

from ..algorithms.random import Random


def set_name(driver):
    if str.lower(driver) == "human":
        return "snake"
    elif str.lower(driver) == "a*":
        return "astar"
    elif str.lower(driver) == "random":
        return "random"
    else:
        return "others"


class Snake:
    def __init__(self, driver="human", color=Config.DEFAULT_SNAKE_COLOR, canvas=None, food=None, obstacles=None):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.name = set_name(driver)
        self.color = color
        self.canvas = canvas
        self.food = food
        self.eaten = True
        self.driver = driver  # human or astar, etc.
        self.score = 0
        self.obstacles = obstacles
        # for obstacle in self.canvas.find_withtag("obstacle"):
        #     self.obstacles.append(self.canvas.coords(obstacle))
        self.path = []
        print(f"Snake {self.name} created with {self.driver} snake {self.snake}")

    def move(self, snake=None, food=None):
        new_head = None
        if self.driver == "human":
            head = self.snake[0]
            if self.direction == "Right":
                new_head = (head[0] + 20, head[1])
            elif self.direction == "Left":
                new_head = (head[0] - 20, head[1])
            elif self.direction == "Up":
                new_head = (head[0], head[1] - 20)
            elif self.direction == "Down":
                new_head = (head[0], head[1] + 20)
        elif self.driver == "Random":
            print("Using Random")
            random_driver = Random()
            self.direction = random_driver.move(food, self.snake)
            head = self.snake[0]
            if self.direction == "Right":
                new_head = (head[0] + 20, head[1])
            elif self.direction == "Left":
                new_head = (head[0] - 20, head[1])
            elif self.direction == "Up":
                new_head = (head[0], head[1] - 20)
            elif self.direction == "Down":
                new_head = (head[0], head[1] + 20)
            del random_driver
        elif self.driver == "A*":
            if self.path or len(self.path) > 0:
                print(f"Using A* with path {self.path}")
                new_head = self.path.pop(0)
            else:
                print("Using A*")
                astar = AStar(snake, food, self.obstacles)
                path = astar.get_path()
                if path == None:
                    print("No path found")
                    return
                self.path = path[::-1]
                new_head = self.path.pop(0)
                del astar
        elif self.driver == "Greedy":
            if self.path:
                new_head = self.path.pop(0)
            else:
                print("Using Greedy")
                greedy = Greedy(snake, food, self.obstacles)
                path = greedy.get_path()
                self.path = path[::-1]
                new_head = self.path.pop(0)
                del greedy

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

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def path_reset(self):
        print(f"Path reset for {self.name}")
        del self.path
        self.path = []