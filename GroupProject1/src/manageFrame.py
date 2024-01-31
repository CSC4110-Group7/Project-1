from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from csvReaderWriter import readCsv, deleteData, validateData
from csvReaderWriter import saveCsv
from csvReaderWriter import columnNames, data


from queryFrame import setViewOutput

def getManageFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Manage', padding=20).pack();

    saveload_frame = ttk.Frame(master=frame, padding=10)
    ttk.Button(master=saveload_frame, text='Load Data', command=openFileButton, padding=10).pack(side=LEFT)
    ttk.Button(master=saveload_frame, text="Save Data", command=saveFileButton, padding=10).pack(side=RIGHT)
    saveload_frame.pack(side=TOP)

    # Frame for delete functionality
    delete_frame = ttk.Frame(master=frame, padding=10)
    ttk.Label(master=delete_frame, text="Unique ID:").pack(side=LEFT)
    unique_id_entry = ttk.Entry(master=delete_frame)
    unique_id_entry.pack(side=LEFT)
    ttk.Button(master=delete_frame, text="Delete", command=lambda: deleteButton(unique_id_entry.get()), padding=10).pack(side=RIGHT)
    delete_frame.pack(side=BOTTOM)

    return frame

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