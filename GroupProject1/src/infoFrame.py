import tkinter as tk
from tkinter import ttk
from scrollTextDisplay import ScrollTextDisplay
import os

#Read license content from file
def ReadInfoFile():
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, 'info.txt')
    with open(filepath, 'r') as file:
        content = '\n'.join([line.strip() for line in file.readlines()])
    file.close()
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


def getInfoFrame(main_frame):
    #Read license content from file
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, 'info.txt')
    file = open(filepath, 'r')
    content = ""
    for line in file:
        content += line
    file.close()

    frame = ttk.Frame(main_frame, padding=10)
    ttk.Label(master=frame, text='Usage Info').pack()
    ttk.Label(master=frame, text=content).pack()

    return frame