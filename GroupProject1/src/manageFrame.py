import tkinter as tk
from tkinter import ttk, filedialog

from csvReaderWriter import readCsv, saveCsv


class ManageFrame:
    def __init__(self, parent, opFrame):
        self.root = ttk.Frame(parent, padding=10)
        self.opFrame = opFrame

        self.title = ttk.Label(self.root, text="Database Management Menu").pack()

        self.save_load_frame = ttk.Frame(self.root, padding=20)
        ttk.Label(self.save_load_frame, text="File Operation", padding=10).pack()
        self.load_button = ttk.Button(self.save_load_frame, text='Load Data', command=self.openFileButton, padding=10).pack(side=tk.LEFT)
        self.save_button = ttk.Button(self.save_load_frame, text='Save Data', command=saveFileButton, padding=10).pack(side=tk.RIGHT)
        self.save_load_frame.pack()


    def pack(self, **kwargs):
        self.root.pack(kwargs)
        
    def openFileButton(self):
        file = filedialog.askopenfile()
        if file:
            table = readCsv(file)
            self.opFrame.setViewOutput(colNames=table.colnames, rows=table.rows)



def saveFileButton():
    file = filedialog.asksaveasfile()
    if file:
        saveCsv(file)