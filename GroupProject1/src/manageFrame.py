import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

from csvReaderWriter import readCsv, deleteData, validateData
from csvReaderWriter import saveCsv
from csvReaderWriter import columnNames, data

from queryFrame import setViewOutput

class ManageFrame:
    def __init__(self, parent):
        self.root = ttk.Frame(parent, padding=10)

        self.title = ttk.Label(self.root, text="Database Management Menu").pack()

        self.save_load_frame = ttk.Frame(self.root, padding=20)
        ttk.Label(self.save_load_frame, text="File Operation", padding=10).pack()
        self.load_button = ttk.Button(self.save_load_frame, text='Load Data', command=openFileButton, padding=10).pack(side=tk.LEFT)
        self.save_button = ttk.Button(self.save_load_frame, text='Save Data', command=saveFileButton, padding=10).pack(side=tk.RIGHT)
        self.save_load_frame.pack()

        # Frame for delete functionality
        # delete_frame = ttk.Frame(self.root, padding=10)
        # ttk.Label(master=delete_frame, text="Unique ID:").pack(side=tk.LEFT)
        # unique_id_entry = ttk.Entry(master=delete_frame)
        # unique_id_entry.pack(side=tk.LEFT)
        # ttk.Button(master=delete_frame, text="Delete", command=lambda: deleteButton(unique_id_entry.get()), padding=10).pack(side=tk.RIGHT)
        # delete_frame.pack(side=tk.BOTTOM)


    def pack(self, **kwargs):
        self.root.pack(kwargs)



def openFileButton():
    file = filedialog.askopenfile()
    if file:
        readCsv(file)
    setViewOutput(colNames=columnNames, rows=data)

def saveFileButton():
    file = filedialog.asksaveasfile()
    if file:
        saveCsv(file)

def deleteButton(uniqueId):
    deleteData(uniqueId)
    messagebox.showinfo("Success", "Record deleted successfully.")