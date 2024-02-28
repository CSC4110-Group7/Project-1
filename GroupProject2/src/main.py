from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from SnakeGame import Game

class MainInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("ForestSnake")
        self.root.geometry("800x500")

        self.license = LicenseConfirmFrame(self.root, self.packAfterAgree)
        self.license.pack()

        self.game = Game(self.root)

    def packAfterAgree(self):
        self.game.canvas.pack(expand=1, fill="both")
        self.game.unpause()

    def mainloop(self):
        self.game.update()
        self.root.mainloop()

def main():
    interface = MainInterface()
    interface.mainloop()

if __name__ == "__main__":
    main()