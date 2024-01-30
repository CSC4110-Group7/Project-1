from tkinter import *
from tkinter import ttk
import os

def getLicenseFrame(window, agreementCallback):
    
    #Read license content from file
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, 'license.txt')
    file = open(filepath, 'r')
    content = ""
    for line in file:
        content += line
    file.close()

    frame = ttk.Frame(window, padding=10)
    ttk.Label(master=frame, text='User License Agreement').pack()
    ttk.Label(master=frame, text=content).pack()

    ttk.Button(master=frame, text='I Agree', command=agreementCallback).pack()

    return frame