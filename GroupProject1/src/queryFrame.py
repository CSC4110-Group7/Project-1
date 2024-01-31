from tkinter import ttk
from tkinter import *


global output_listbox

def getQueryFrame(main_frame):
    global output_listbox

    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Query', padding=20).pack();

    output_frame = ttk.Frame(master=frame, padding=10)
    output_scrollbar = ttk.Scrollbar(master=output_frame, orient='vertical')
    output_listbox = Listbox(master=output_frame, width=100, font="TkFixedFont")

    #Link scrollbar & output box together
    output_listbox.config(yscrollcommand = output_scrollbar.set);
    output_scrollbar.config(command=output_listbox.yview);

    output_scrollbar.pack(side=RIGHT, fill=BOTH);
    output_listbox.pack(side=LEFT, fill=BOTH);
    output_frame.pack(side=BOTTOM);

    return frame

def setViewOutput(colNames, rows):
    output_listbox.delete(0, END)

    row_format = '    '.join(['{:<' + str(len(name)) + '}' for name in colNames])
    print(row_format)

    output_listbox.insert(END, row_format.format(*colNames))

    for row in rows:
        output_listbox.insert(END, row_format.format(*row))