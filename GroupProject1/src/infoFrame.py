import tkinter as tk
from tkinter import ttk
from scrollTextDisplay import ScrollTextDisplay
from info import info

#Read license content from file
def ReadInfoFile():
    # filepath = resource_path('info.txt')
    # with open(filepath, 'r') as file:
    #     content = '\n'.join([line.strip() for line in file.readlines()])
    # file.close()
    content = info
    return content

class InfoFrame:
    def __init__(self, parent):
        self.root = ttk.Frame(parent, padding=10)
        self.info_text = ReadInfoFile()

        self.title = ttk.Label(self.root, text="User Manual").pack()
        self.info = ScrollTextDisplay(self.root, text=self.info_text)
        self.info.pack()

    def pack(self, **kwargs):
        self.root.pack(kwargs)