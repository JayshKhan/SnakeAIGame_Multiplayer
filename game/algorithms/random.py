class Random:
    def __init__(self):
        self.name = "Random"

    def move(self, food_coord, snake_coords):
        # TODO: Implement Random Algorithm which can avoid obstacles and snake itself
        # Current Algorithm is not avoiding the obstacles and snake itself
        head = snake_coords[0]
        if head[0] < food_coord[0]:
            return "Right"
        elif head[0] > food_coord[0]:
            return "Left"
        if head[1] < food_coord[1]:
            return "Down"
        elif head[1] > food_coord[1]:
            return "Up"

        return None
