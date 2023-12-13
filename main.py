from ui.screens.menu import Menu, tk


def main():
    # initialize main menu, Event loop
    root = tk.Tk()
    Menu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
