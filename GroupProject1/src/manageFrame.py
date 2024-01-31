from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from csvReaderWriter import readCsv
from csvReaderWriter import saveCsv
from csvReaderWriter import columnNames, data


from queryFrame import setViewOutput

def getManageFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Manage', padding=20).pack();

    saveload_frame = ttk.Frame(master=frame, padding=10)
    ttk.Button(master=saveload_frame, text='Load Data', command=openFileButton, padding=10).pack(side=LEFT)
    ttk.Button(master=saveload_frame, text="Save Data", command=saveFileButton, padding=10).pack(side=RIGHT)
    saveload_frame.pack(side=BOTTOM)

    return frame

def openFileButton():
    file = filedialog.askopenfile()
    readCsv(file)
    setViewOutput(colNames=columnNames, rows=data)

def saveFileButton():
    file = filedialog.asksaveasfile()
    saveCsv(file)