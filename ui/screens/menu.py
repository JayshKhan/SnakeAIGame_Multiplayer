from game.game import Game
from ui.base import BaseLayout, tk, messagebox
from utils.config import Config


class Menu(BaseLayout):
    def __init__(self, master):
        super().__init__(master)
        self.no_of_players = tk.IntVar()
        self.no_of_players.set(1)
        # using config to get the height and width of the screen
        self.settings_window = None
        self.canvas.create_text(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 4,
                                text=Config.TITLE,
                                font=("Arial", 30),
                                fill=Config.TEXT_COLOR)
        # painting the No of players on top right
        self.player_counter = self.canvas.create_text(Config.SCREEN_WIDTH - 150, 50,
                                                      text=f"Players: {self.no_of_players.get()}",
                                                      font=("Arial", 20),
                                                      fill=Config.TEXT_COLOR)
        # painting the buttons
        self.play_button = tk.Button(self.master,
                                     text="Play",
                                     font=("Arial", 20),
                                     command=self.play)
        self.play_button_window = self.canvas.create_window(Config.SCREEN_WIDTH / 2,
                                                            Config.SCREEN_HEIGHT / 2,
                                                            anchor="center",
                                                            window=self.play_button)
        self.settings_button = tk.Button(self.master,
                                         text="Settings",
                                         font=("Arial", 20),
                                         command=self.settings)
        self.settings_button_window = self.canvas.create_window(Config.SCREEN_WIDTH / 2,
                                                                Config.SCREEN_HEIGHT / 2 + 50,
                                                                anchor="center",
                                                                window=self.settings_button)

        self.quit_button = tk.Button(self.master,
                                     text="Quit",
                                     font=("Arial", 20),
                                     command=self.quit)
        self.quit_button_window = self.canvas.create_window(Config.SCREEN_WIDTH / 2,
                                                            Config.SCREEN_HEIGHT / 2 + 100,
                                                            anchor="center",
                                                            window=self.quit_button)

    def play(self):
        self.master.destroy()
        root = tk.Tk()
        game = Game(root, self.no_of_players.get())
        root.mainloop()

    def settings(self):
        # change the screen size window
        self.settings_window = tk.Toplevel(self.master)
        self.settings_window.title("Settings")
        self.settings_window.geometry("400x400")
        self.settings_window.resizable(False, False)

        # change the no of players
        no_of_players_label = tk.Label(self.settings_window,
                                       text="No of Players",
                                       font=("Arial", 20))
        no_of_players_label.pack()

        # check what is the current value of no of players
        if self.no_of_players == 1:
            no_of_players_radio_button_1 = tk.Radiobutton(self.settings_window,
                                                          text="1",
                                                          font=("Arial", 20),
                                                          variable=self.no_of_players,
                                                          value=1,
                                                          state="active")
            no_of_players_radio_button_1.pack()
            no_of_players_radio_button_2 = tk.Radiobutton(self.settings_window,
                                                          text="2",
                                                          font=("Arial", 20),
                                                          variable=self.no_of_players,
                                                          value=2)
            no_of_players_radio_button_2.pack()
        else:
            no_of_players_radio_button_1 = tk.Radiobutton(self.settings_window,
                                                          text="1",
                                                          font=("Arial", 20),
                                                          variable=self.no_of_players,
                                                          value=1)
            no_of_players_radio_button_1.pack()
            no_of_players_radio_button_2 = tk.Radiobutton(self.settings_window,
                                                          text="2",
                                                          font=("Arial", 20),
                                                          variable=self.no_of_players,
                                                          value=2,
                                                          state="active")
            no_of_players_radio_button_2.pack()

        # save button to quit the settings window
        save_button = tk.Button(self.settings_window,
                                text="Save",
                                font=("Arial", 20),
                                command=self.save_settings)
        save_button.pack()

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
