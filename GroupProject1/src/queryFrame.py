from tkinter import ttk
from tkinter import *

global output_listbox

def getQueryFrame(main_frame):
    global output_listbox

    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Query', padding=20).pack();

    output_frame = ttk.Frame(master=frame, padding=10)
    output_scrollbar = ttk.Scrollbar(master=output_frame, orient='vertical')
    output_listbox = Listbox(master=output_frame, width=100)

    #Link scrollbar & output box together
    output_listbox.config(yscrollcommand = output_scrollbar.set);
    output_scrollbar.config(command=output_listbox.yview);

    output_scrollbar.pack(side=RIGHT, fill=BOTH);
    output_listbox.pack(side=LEFT, fill=BOTH);
    output_frame.pack(side=BOTTOM);

    return frame

def setViewOutput(colNames, rows):
    names = ''
    for name in colNames:
        names += name + (' ' * (20 - len(name)))
    output_listbox.insert(END, names)

    for row in rows:
        row_out = ''
        for value in row:
            row_out += value + (' ' * (20 - len(value)))
        output_listbox.insert(END, row_out)