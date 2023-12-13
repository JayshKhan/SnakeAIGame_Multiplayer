class Config:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 400
    BOARD_SIZE = 20
    GEOMETRY = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"
    SCREEN_SIZES = ["400x400", "600x600"]
    TITLE = "Snake Game"
    BACKGROUND_COLOR = "black"
    TEXT_COLOR = "white"
    DEFAULT_SNAKE_COLOR = "green"
    DEFAULT_FOOD_COLOR = "red"
    OTHER_SNAKE_COLORS = ["yellow", "pink", "orange", "purple"]
    BORDER_COLOR = "white"
    BORDER_WIDTH = 20
    SNAKE_STARTING_POSITION = [(100, 100), (90, 100), (80, 100)]
    SNAKE_STARTING_DIRECTION = "Right"
    SNAKE_STARTING_LENGTH = 3

    # for the enemy snake
