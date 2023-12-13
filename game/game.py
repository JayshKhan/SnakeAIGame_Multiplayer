from .components.obstacle import get_obstacles
from .components.snake import Snake
from .components.food import Food
from ui.base import BaseLayout, tk
from utils.config import Config


class Game(BaseLayout):
    def __init__(self, master, no_of_snakes=1):
        super().__init__(master)
        self.snakes = []
        self.no_of_snakes = no_of_snakes
        self.food = Food(self.canvas)
        self.obstacles = get_obstacles(self.canvas)

        self.score = 0
        self.set_snakes()
        self.master.bind("<KeyPress>", self.change_direction)
        self.update()

    def set_snakes(self):
        if self.no_of_snakes > 1:
            # first is human
            self.snakes.append(Snake())
            remaining = self.no_of_snakes - 1
            for i in range(remaining):
                self.snakes.append(Snake("snake" + str(i + 1), "random", Config.OTHER_SNAKE_COLORS[i + 1]))

        else:
            self.snakes.append(Snake())

    def update(self):
        food_coords = self.food.get_food_coords()
        for snake in self.snakes:
            snake.move()
            head = snake.get_snake()[0]
            snake.paint_snake(self.canvas)
            if snake.get_driver() == "human":
                self.check_game_over(head)
            if head[0] == food_coords[0] and head[1] == food_coords[1]:
                snake.get_snake().append((0, 0))
                self.canvas.delete("food")
                self.food.paint(self.canvas)

        self.master.after(200, self.update)

    def change_direction(self, event):
        if event.keysym == "Right" and not self.snakes[0].get_direction() == "Left":
            self.snakes[0].set_direction("Right")
        elif event.keysym == "Left" and not self.snakes[0].get_direction() == "Right":
            self.snakes[0].set_direction("Left")
        elif event.keysym == "Up" and not self.snakes[0].get_direction() == "Down":
            self.snakes[0].set_direction("Up")
        elif event.keysym == "Down" and not self.snakes[0].get_direction() == "Up":
            self.snakes[0].set_direction("Down")

    def check_game_over(self, head):
        if head[0] < 0 or head[0] > Config.SCREEN_WIDTH - 20 or head[1] < 0 or head[1] > Config.SCREEN_HEIGHT - 20:
            self.game_over()
            return

        # check if the snake hits itself
        for segment in self.snakes[0].get_snake()[1:]:
            if head[0] == segment[0] and head[1] == segment[1]:
                self.game_over()
                return

        # check if the snake hits the obstacle
        for obstacle in self.obstacles:
            obstacle_coords = self.canvas.coords(obstacle)
            if head[0] == obstacle_coords[0] and head[1] == obstacle_coords[1]:
                self.game_over()
                return

    def game_over(self):
        for snake in self.snakes:
            self.snakes.remove(snake)
        self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                Config.SCREEN_HEIGHT / 2,
                                anchor="center", text="Game Over", font=("Arial", 30), fill="white")
        self.canvas.create_text(Config.SCREEN_WIDTH / 2,
                                Config.SCREEN_HEIGHT / 2 + 50,
                                anchor="center", text="Press Space to Restart", font=("Arial", 20), fill="white")
        self.master.bind("<space>", self.restart)
        return

    def restart(self, event):
        self.master.destroy()
        root = tk.Tk()
        game = Game(root, self.no_of_snakes)
        root.mainloop()
