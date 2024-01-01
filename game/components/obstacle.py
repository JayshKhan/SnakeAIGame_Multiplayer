import random


def get_obstacles(canvas):
    obstacle = []
    obstacle_coords = []
    for i in range(18):
        x = random.randint(1, 18) * 20
        y = random.randint(1, 18) * 20
        # check if the obstacle is not on the food
        food = canvas.gettags("food")
        food_coords = canvas.coords(food[0])
        if x == food_coords[0] and y == food_coords[1] or x + 20 == food_coords[0] and y + 20 == food_coords[1]:
            continue
        # check if the obstacle is not on the snake
        continue_loop = False
        snake_coords = [(120, 100), (100, 100), (90, 100), (80, 100)]
        for snake_coord in snake_coords:
            if x == snake_coord[0] and y == snake_coord[1] or x + 20 == snake_coord[0] and y + 20 == snake_coord[1]:
                continue_loop = True
                break
        if continue_loop:
            continue
        obstacle.append(canvas.create_rectangle(x, y, x + 20, y + 20, fill="blue", tags="obstacle"))
        obstacle_coords.append((x, y))

    return obstacle, obstacle_coords
