# creates an Extra Window to display the score of the game for both players
import tkinter as tk
from tkinter import ttk


class ScoreBoard(tk.Toplevel):
    def __init__(self,no_of_snakes=1):
        super().__init__()
        self.no_of_snakes = no_of_snakes
        self.title("Score Board")
        x= self.winfo_screenwidth()
        y= self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d' % (280, 50, x, y))
        self.resizable(False, False)
        self.score = 0
        self.score2 = 0
        self.score_label = None
        self.score_label2 = None
        self.create_widgets()

    def create_widgets(self):
        self.score_label = ttk.Label(self, text="Score Player 1: {}".format(self.score))
        self.score_label.grid(row=0, column=0, padx=10, pady=10)
        if self.no_of_snakes > 1:
            self.score_label2 = ttk.Label(self, text="Score Player 2: {}".format(self.score2))
            self.score_label2.grid(row=0, column=1, padx=10, pady=10)

    def reset_score(self):
        self.score = 0
        self.score_label.config(text="Score Player 1: {}".format(self.score))
        if self.no_of_snakes > 1:
            self.score2 = 0
            self.score_label2.config(text="Score Player 2: {}".format(self.score2))

    def update_scoreboard(self, score, score2):
        self.score = score
        self.score_label.config(text="Score Player 1: {}".format(self.score))
        if self.no_of_snakes > 1:
            self.score2 = score2
            self.score_label2.config(text="Score Player 2: {}".format(self.score2))
