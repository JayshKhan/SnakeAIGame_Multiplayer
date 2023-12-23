from ui.screens.menu import Menu, tk

from customtkinter import *


def main():
    # initialize main menu, Event loop
    app = CTk()
    Menu(app)
    app.mainloop()
    # root = tk.Tk()
    # Menu(root)
    # root.mainloop()


if __name__ == "__main__":
    main()
