from customtkinter import *

from ui.screens.menu import Menu


def main():
    app = CTk()
    Menu(app)
    app.mainloop()


if __name__ == "__main__":
    main()
