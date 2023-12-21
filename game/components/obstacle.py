import random


def get_obstacles(canvas):
    obstacle = []
    for i in range(10):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        # check if the obstacle is not on the food
        food = canvas.gettags("food")
        food_coords = canvas.coords(food[0])
        if x == food_coords[0] and y == food_coords[1] or x+20 == food_coords[0] and y+20 == food_coords[1]:
            continue
        obstacle.append(canvas.create_rectangle(x, y, x + 20, y + 20, fill="blue", tags="obstacle"))

    return obstacle
