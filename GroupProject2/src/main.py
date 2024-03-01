from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from launchFrame import LaunchFrame
from TurtleSnake import game


class MainInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("ForestSnake")
        # self.root.geometry("800x500")
        self.root.protocol("WM_DELETE_WINDOW", self.onWindowClose)

        self.license = LicenseConfirmFrame(self.root, self.packAfterAgree)
        self.license.pack()
        
        self.launch_frame = LaunchFrame(self.root, self.launchGame)

        # self.game = Game(self.root)
        

    def packAfterAgree(self):
        # self.game.canvas.pack(expand=1, fill="both")
        # self.game.unpause()
        self.license.root.pack_forget()
        self.launch_frame.root.pack()
        
        
    def launchGame(self):
        self.root.destroy()
        game()

    def mainloop(self):
        # self.game.start()
        self.root.mainloop()
        
    def onWindowClose(self):
        # self.game.running = False
        # self.root.destroy()
        pass

def main():
    interface = MainInterface()
    interface.mainloop()

if __name__ == "__main__":
    main()