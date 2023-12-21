# from utils.config import Config
#
#
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
        self.open_set.append(self.snake_coords[0])
        self.g_score[self.snake_coords[0]] = 0
        self.f_score[self.snake_coords[0]] = self.heuristic(self.snake_coords[0])

        while len(self.open_set) > 0:
            current = self.get_lowest_f_score()
            if current == self.food_coords:
                self.path_found = True
                return self.reconstruct_path(current)

            self.open_set.remove(current)
            self.closed_set.append(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = self.g_score[current] + 1

                if neighbor not in self.open_set:
                    self.open_set.append(neighbor)
                elif tentative_g_score >= self.g_score[neighbor]:
                    continue

                self.came_from[neighbor] = current
                self.g_score[neighbor] = tentative_g_score
                self.f_score[neighbor] = self.g_score[neighbor] + self.heuristic(neighbor)

        return None

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


