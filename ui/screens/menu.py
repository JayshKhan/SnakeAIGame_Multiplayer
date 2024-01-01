import tkinter as tk
from tkinter import messagebox

import customtkinter
from customtkinter import *

from game.game import Game
from ui.base import BaseLayout
from utils.config import Config


class Menu(BaseLayout):
    def __init__(self, master):
        super().__init__(master)
        self.no_of_players = customtkinter.IntVar()
        self.ai_algorithm = customtkinter.StringVar()
        self.no_of_players.set(2)
        self.ai_algorithm.set("A*")
        # using config to get the height and width of the screen
        self.settings_window = None
        self.no_of_players_btn = CTkSwitch(self.settings_window, variable=self.no_of_players,
                                           text="Single Players" if self.no_of_players == 1 else "Multiplayer",
                                           onvalue="2", offvalue="1")
        self.ai_algorithm_btn = CTkOptionMenu(self.settings_window, variable=self.ai_algorithm,
                                              values=["A*", "Greedy", "Random"])
        self.canvas.create_text(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 4,
                                text=Config.TITLE,
                                font=("Arial", 30),
                                fill=Config.TEXT_COLOR)
        # painting the No of players on top right
        self.player_counter = self.canvas.create_text(Config.SCREEN_WIDTH - 150, 50,
                                                      text=f"Players: {self.no_of_players.get()}",
                                                      font=("Arial", 20),
                                                      fill=Config.TEXT_COLOR)

        self.play_button = CTkButton(self.master, text="Play", font=("Arial", 20), command=self.play)
        self.play_button.place(x=Config.SCREEN_WIDTH / 2, y=Config.SCREEN_HEIGHT / 2, anchor="center")

        self.settings_button = CTkButton(self.master, text="Settings", font=("Arial", 20), command=self.settings)
        self.settings_button.place(x=Config.SCREEN_WIDTH / 2, y=Config.SCREEN_HEIGHT / 2 + 50, anchor="center")

        self.quit_button = CTkButton(self.master, text="Quit", font=("Arial", 20), command=self.quit)
        self.quit_button.place(x=Config.SCREEN_WIDTH / 2, y=Config.SCREEN_HEIGHT / 2 + 100, anchor="center")

    def play(self):
        self.master.destroy()
        root = tk.Tk()
        game = Game(root, self.no_of_players.get(), self.ai_algorithm.get())
        root.mainloop()

    def settings(self):
        # change the screen size window
        self.settings_window = CTkToplevel()
        self.settings_window.title("Settings")
        self.settings_window.geometry("400x400")
        self.settings_window.resizable(False, False)

        setting_label = CTkLabel(self.settings_window, text="Settings", font=("Arial", 20))
        setting_label.place(x=200, y=50, anchor="center")

        # change the no of players
        # no_of_players_label = tk.Label(self.settings_window,
        #                                text="No of Players",
        #                                font=("Arial", 20))
        # no_of_players_label.pack()

        self.no_of_players_btn = CTkSwitch(self.settings_window, variable=self.no_of_players,
                                           text="Multiplayer",
                                           onvalue=2, offvalue=1)
        self.no_of_players_btn.place(x=200, y=100, anchor="center")

        # change the ai algorithm
        ai_algorithm_label = CTkLabel(self.settings_window,
                                      text="AI Algorithm",
                                      font=("Arial", 20))
        ai_algorithm_label.place(x=200, y=150, anchor="center")

        self.ai_algorithm_btn = CTkOptionMenu(self.settings_window, variable=self.ai_algorithm,
                                              values=["A*", "Greedy", "Random"])
        self.ai_algorithm_btn.place(x=200, y=200, anchor="center")

        # save the settings
        save_button = CTkButton(self.settings_window, text="Save", font=("Arial", 20), command=self.save_settings)
        save_button.place(x=200, y=300, anchor="center")

    def save_settings(self):
        self.settings_window.destroy()
        self.master.update()
        # update the current screen
        self.canvas.delete(self.player_counter)
        self.player_counter = self.canvas.create_text(Config.SCREEN_WIDTH - 150, 50,
                                                      text=f"Players: {self.no_of_players.get()}",
                                                      font=("Arial", 20),
                                                      fill=Config.TEXT_COLOR)

    def quit(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.master.destroy()
