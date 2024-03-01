from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from launchFrame import LaunchFrame
from SnakeGame import Game
import importlib

def execute_python_file(file_path):
   try:
      module_name = file_path.replace('.py', '')  # Remove the '.py' extension
      module = importlib.import_module(module_name)
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")
   except ModuleNotFoundError:
      print(f"Error: The module '{module_name}' could not be found.")
   except ImportError as e:
      print(f"Error: Unable to import '{module_name}': {e}")

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
        execute_python_file("TurtleSnake.py")

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