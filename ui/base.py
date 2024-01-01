import tkinter as tk

from utils.config import Config


class BaseLayout:
    def __init__(self, master):
        # use config to get the values and set them
        self.master = master
        self.master.title(Config.TITLE)
        self.master.resizable(False, False)
        self.master.geometry(Config.GEOMETRY)

        self.canvas = tk.Canvas(self.master,
                                bg=Config.BACKGROUND_COLOR,
                                width=Config.SCREEN_WIDTH,
                                height=Config.SCREEN_HEIGHT)

        self.canvas.pack()
