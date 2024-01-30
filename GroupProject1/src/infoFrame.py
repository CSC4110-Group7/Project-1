from tkinter import *
from tkinter import ttk
import os

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