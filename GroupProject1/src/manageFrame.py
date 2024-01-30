from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import filedialog

from csvReaderWriter import readCsv
from csvReaderWriter import columnNames
from csvReaderWriter import data

def getManageFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Manage', padding=20).pack();
    
    ttk.Button(master=frame, text='Open Data', command=openFileButton).pack()

    return frame

def openFileButton():
    file = filedialog.askopenfile()
    readCsv(file)
    print(columnNames)
    print(data)