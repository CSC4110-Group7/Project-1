from tkinter import ttk
from tkinter import *

from csvReaderWriter import columnNames, data, types, validate


def getQueryFrame(main_frame):
    global output_listbox, action_type, field_type, input_entry, input_entry2

    query_frame = ttk.Frame(master=main_frame)
    ttk.Label(master=query_frame, text='Query', padding=20).pack();

    output_frame = ttk.Frame(master=query_frame, padding=10)
    output_scrollbar = ttk.Scrollbar(master=output_frame, orient="vertical")
    output_listbox = Listbox(master=output_frame, width=100, font="TkFixedFont")

    #Link scrollbar & output box together
    output_listbox.config(yscrollcommand = output_scrollbar.set);
    output_scrollbar.config(command=output_listbox.yview);

    output_scrollbar.pack(side=RIGHT, fill=BOTH);
    output_listbox.pack(side=LEFT, fill=BOTH);
    output_frame.pack(side=BOTTOM);

    input_frame = ttk.Frame(master=query_frame, padding=10)
    query_button = ttk.Button(master=input_frame, text='Query', command=handleExecute)

    action_type = StringVar(input_frame)
    action_type.set('query')
    action_type_option = ttk.OptionMenu(input_frame, action_type, *['query', 'query', 'delete', 'insert', 'update'])

    input_entry = ttk.Entry(input_frame, width=30)
    input_entry2 = ttk.Entry(input_frame, width=30)


    input_frame.pack(side=BOTTOM)
    query_button.pack(side=LEFT)
    action_type_option.pack(side=LEFT)
    input_entry.pack(side=LEFT)
    input_entry2.pack(side=LEFT)

    return query_frame


def handleExecute():

    #Parse query
    query_fields = []
    query_values = []
    for t in input_entry.get().split(','):
        if(len(t.split(':')) != 2):
            continue
        query_fields.append(t.split(':')[0])
        query_values.append(t.split(':')[1])

    #Parse update
    modify_fields = []
    modify_values = []
    if(len(input_entry2.get()) > 0):
        for t in input_entry2.get().split(','):
            if(len(t.split(':')) != 2):
                continue
            modify_fields.append(t.split(':')[0])
            modify_values.append(t.split(':')[1])

    #Validate query
    valid = True
    for i, query_field in enumerate(query_fields):
        field_index = columnNames.index(query_field)
        if(field_index < 0):
            valid = False
            break
        if(not validate(query_values[i], types[i])):
            valid = False
            break
    
    #Validate update
    for i, modify_field in enumerate(modify_fields):
        field_index = columnNames.index(modify_field)
        if(field_index < 0):
            valid = False
            break
        if(not validate(modify_values[i], types[i])):
            valid = False
            break
    
    #Do nothing if either query or update is invalid
    if(not valid):
        return
    
    #Select rows that match
    selected = []
    for i, row in enumerate(data):
        select = True

        for j, query_field in enumerate(query_fields):
            query_index = columnNames.index(query_field)
            if(row[query_index] != query_values[j]):
                select=False
                continue

        if(select):
            selected.append(i)

    action = action_type.get()
    if(action == 'query'):
        view = []
        for i in selected:
            view.append(data[i])
        setViewOutput(columnNames, view)



def setViewOutput(colNames, rows):
    output_listbox.delete(0, END)

    row_format = '    '.join(['{:<' + str(len(name)) + '}' for name in colNames])

    output_listbox.insert(END, row_format.format(*colNames))

    for row in rows:
        output_listbox.insert(END, row_format.format(*row))