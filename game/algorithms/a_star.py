from utils.config import Config


class AStar:
    def __init__(self, snake, food):
        # TODO: Obstacles
        self.snake_coords = snake
        self.food_coords = food

        self.path = []
        self.path_found = False
        self.path_index = 0
        self.closed_set = []
        self.open_set = []
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

        self.path = self.get_path()

    def get_obstacles(self):
        for obstacle in self.canvas.find_withtag("obstacle"):
            self.obstacles.append(self.canvas.coords(obstacle))

    def get_path(self):
        # TODO: get path Using AStar Algo with (x,y) coordinates
        pass

    def heuristic(self, param):
        pass

    def get_neighbors(self, current):
        pass

    def get_lowest_f_score(self):
        pass

    def reconstruct_path(self, current):
        pass

    def get_next_direction(self):
        pass
