from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from csvReaderWriter import readCsv
from csvReaderWriter import saveCsv

def getManageFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Manage', padding=20).pack();
    
    ttk.Button(master=frame, text='Load Data', command=openFileButton).pack()
    ttk.Button(master=frame, text="Save Data", command=saveFileButton).pack()

    return frame

def openFileButton():
    file = filedialog.askopenfile()
    readCsv(file)

def saveFileButton():
    file = filedialog.asksaveasfile()
    saveCsv(file)