import random


class Food:
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.color = (255, 0, 0)
        self.size = 10
        self.randomize()
        self.paint(canvas)

    def randomize(self):
        self.x = random.randint(0, 19) * 20
        self.y = random.randint(0, 19) * 20

    def paint(self, canvas):
        self.randomize()
        print(f"food_coords from food: {self.x, self.y}")
        canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="red", tags="food")

    def get_food_coords(self):
        return self.x, self.y
