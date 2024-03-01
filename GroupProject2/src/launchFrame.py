import tkinter as tk



class LaunchFrame:
    def __init__(self, parent, launchGameCallback):
        self.parent = parent
        self.root = tk.Frame(master=parent, padx=20, pady=20)
        
        tk.Label(self.root, text="Official Snake Game Launcher").pack()
        
        self.launch_button = tk.Button(self.root, text='Launch Game', command=launchGameCallback)
        self.launch_button.pack()
        
        self.instruction_frame = tk.Frame(master=self.root, pady=10)
        tk.Label(self.instruction_frame, text='Instructions').pack()
        tk.Label(self.instruction_frame, text='Use wasd to move your snake').pack()
        tk.Label(self.instruction_frame, text='Collect apples to increase your score').pack()
        tk.Label(self.instruction_frame, text='Do not run into yourself or the walls').pack()
        self.instruction_frame.pack(side='left', expand=1, fill='x')

        