from tkinter import *
from tkinter import ttk

def getManageFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Manage', padding=20).pack();
    return frame