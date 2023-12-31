import random


class AStar:
    def __init__(self, snake, food, obstacles=None):

        self.obstacles = obstacles
        self.obstacles_coords = []
        self.get_obstacle_coords()
        self.snake_coords = snake[0]
        self.snake = snake
        self.food_coords = food
        self.obstacles = []
        self.path = []
        self.path_found = False
        self.path_index = 0
        self.closed_set = []
        self.open_set = []
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

        self.path = self.get_path()


    def get_path(self):
        self.open_set.append(self.snake_coords)
        self.g_score[self.snake_coords] = 0
        self.f_score[self.snake_coords] = self.heuristic(self.snake_coords)

        while self.open_set:
            current = self.get_lowest_f_score()
            # print(f"Current: {current}")
            if current == self.food_coords:
                # print("Path found!")
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

        return []

    def heuristic(self, snake_coords):
        return (abs(snake_coords[0] -
                    self.food_coords[0]) +
                abs(snake_coords[1] -
                    self.food_coords[1]))

    def get_neighbors(self, current):
        neighbors = []
        moves = [(0, 20), (0, -20), (20, 0), (-20, 0)]

        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])
            remove = False

            # Check if the neighbor is within the boundaries of the game
            if 0 <= neighbor[0] <= 380 and 0 <= neighbor[1] <= 380:
                neighbors.append(neighbor)
                # check if the neighbor is not on the obstacle
                for obstacle in self.obstacles_coords:
                    if neighbor[0] == obstacle[0] and neighbor[1] == obstacle[1]:
                        remove = True
                # Check if the neighbor is not in the entire snake's body
                for segment in self.snake:
                    if neighbor[0] == segment[0] and neighbor[1] == segment[1]:
                        remove = True
                if remove:
                    neighbors.remove(neighbor)

        return neighbors

    def get_lowest_f_score(self):
        lowest_f_score_node = None
        lowest_f_score = float('inf')
        for node in self.open_set:
            if self.f_score[node] < lowest_f_score:
                lowest_f_score = self.f_score[node]
                lowest_f_score_node = node
        return lowest_f_score_node

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from.keys():
            current = self.came_from[current]
            total_path.append(current)
        # check two arrays if they have any common elements
        if self.obstacles_coords:
            for obstacle in self.obstacles_coords:
                if obstacle in total_path or (obstacle[0] + 20, obstacle[1] + 20) in total_path:
                    print("Obstacle in path")
                    break
        return total_path

    def get_obstacle_coords(self):
        self.obstacles_coords = self.obstacles
        # for obstacle in self.obstacles:
        #     self.obstacles_coords.append((obstacle[0] + 20, obstacle[1] + 20))
        return self.obstacles_coords

    def get_next_direction(self):
        if self.path_index < len(self.path):
            next_node = self.path[self.path_index]
            self.path_index += 1
            if next_node[0] > self.snake_coords[0]:
                return "Right"
            elif next_node[0] < self.snake_coords[0]:
                return "Left"
            elif next_node[1] < self.snake_coords[1]:
                return "Up"
            elif next_node[1] > self.snake_coords[1]:
                return "Down"
        # in case the path is not found return random direction
        return random.choice(["Right", "Left", "Up", "Down"])
