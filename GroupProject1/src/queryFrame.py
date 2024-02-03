from tkinter import ttk
from tkinter import *
import tkinter as tk

from csvReaderWriter import table
from scrollTextDisplay import ScrollListDisplay, ScrollTextDisplay
from database import parseSelectQuery, parseAssignQuery, parseInsertion


class OperationFrame:
    def __init__(self, parent):
        self.root = ttk.Frame(parent, padding=10)
        ttk.Label(self.root, text="Database Operations").pack()
        
        self.output_frame = ttk.Frame(self.root)
        self.output = ScrollListDisplay(self.output_frame)
        
        self.operation_select_frame = ttk.Frame(self.root)
        self.execute_button = ttk.Button(self.operation_select_frame, text='Execute', command=self.executeOperation)
        
        self.operation_var = StringVar(self.operation_select_frame)
        self.operation_var.set('query')
        self.operation_dropdown = ttk.OptionMenu(self.operation_select_frame, self.operation_var, *['query', 'query', 'delete', 'insert', 'update'])
        tk.Label(self.operation_select_frame, text="Operation: ").pack(side=LEFT)
        self.operation_dropdown.pack(side=LEFT)
        self.execute_button.pack(side=LEFT)
        self.operation_select_frame.pack(fill=tk.X)
        
        self.input_frame = ttk.Frame(self.root)
        self.selection = OperationInput(self.input_frame, 'Select')
        self.selection.root.grid(column=1)
        
        self.operation_var.trace_add('write', callback=self.changeOperation)
        
        self.modification = OperationInput(self.input_frame, 'Modify')
        
        self.input_frame.pack(expand=1)
        tk.Label(self.output_frame, text="Result").pack(fill=tk.X)
        self.output.pack(fill=tk.X)
        self.output_frame.pack(fill=tk.X)
        
    def getSelection(self):
        return self.selection.read()
    
    def getModification(self):
        return self.modification.read()
        
    def changeOperation(self, *args):
        newop = self.operation_var.get()
        
        self.selection.input.textbox.config(width=90)
        self.selection.root.grid_forget()
        self.modification.input.textbox.config(width=90)
        self.modification.root.grid_forget()
        
        if(newop == 'query'):
            self.selection.root.grid(column=1)
        elif(newop == 'delete'):
            self.selection.root.grid(column=1)
        elif(newop == 'insert'):
            self.modification.root.grid(column=1)
        elif(newop == 'update'):
            self.selection.root.grid(row=1, column=1)
            self.selection.input.textbox.config(width=45)
            self.modification.root.grid(row=1, column=2)
            self.modification.input.textbox.config(width=45)
        
        print(f'Changing operation to {newop}')
        
    def executeOperation(self):
        operation = self.operation_var.get()
        print(f'Executing operation {operation}')
        
        selection_options = parseSelectQuery(self.selection.read())
        assignment_options = parseAssignQuery(self.modification.read())
        
        if(operation == 'query'):
            rows = table.select(selection_options)
            self.setViewOutput(table.colnames, rows)
        elif(operation == 'delete'):
            table.delete(selection_options)
            self.setViewOutput(table.colnames, table.rows)
        elif(operation == 'update'):
            affected = table.update(selection_options, assignment_options)
            self.setViewOutput(table.colnames, affected)
        elif(operation == 'insert'):
            row_to_insert = parseInsertion(self.modification.read())
            table.insert(row_to_insert)
            self.setViewOutput(table.colnames, table.rows)
        
    # def executeOperation(self):
    #     operation = self.operation_var.get()
    #     print(f'Executing operation {operation}')
        
    #     #Parse query
    #     query_fields = []
    #     query_values = []
    #     for t in self.selection.read().split(','):
    #         if(len(t.split(':')) != 2):
    #             continue
    #         query_fields.append(t.split(':')[0])
    #         query_values.append(t.split(':')[1])

    #     #Parse update
    #     modify_fields = []
    #     modify_values = []
    #     if(len(self.modification.read()) > 0):
    #         for t in self.modification.read().split(','):
    #             if(len(t.split(':')) != 2):
    #                 continue
    #             modify_fields.append(t.split(':')[0])
    #             modify_values.append(t.split(':')[1])

    #     #Validate query
    #     valid = True
    #     for i, query_field in enumerate(query_fields):
    #         field_index = columnNames.index(query_field)
    #         if(field_index < 0):
    #             valid = False
    #             break
    #         if(not validate(query_values[i], types[i])):
    #             valid = False
    #             break
        
    #     #Validate update
    #     for i, modify_field in enumerate(modify_fields):
    #         field_index = columnNames.index(modify_field)
    #         if(field_index < 0):
    #             valid = False
    #             break
    #         if(not validate(modify_values[i], types[i])):
    #             valid = False
    #             break
        
    #     #Do nothing if either query or update is invalid
    #     if(not valid):
    #         return
        
    #     #Select rows that match
    #     selected = []
    #     for i, row in enumerate(data):
    #         select = True

    #         for j, query_field in enumerate(query_fields):
    #             query_index = columnNames.index(query_field)
    #             if(row[query_index] != query_values[j]):
    #                 select=False
    #                 continue

    #         if(select):
    #             selected.append(i)

    #     action = self.operation_var.get()
    #     if(action == 'query'):
    #         view = []
    #         for i in selected:
    #             view.append(data[i])
    #         self.setViewOutput(columnNames, view)
            
    def setViewOutput(self, colNames, rows):
        self.output.clear()
        col_widths = [len(name)+5 for name in colNames]
        col_formats = ['{:<' + str(col_width) + '}' for col_width in col_widths]
        
        row_format = ' | '.join(col_formats)
        self.output.insert(row_format.format(*colNames))

        for row in rows:
            self.output.insert(row_format.format(*row))
    
        
    def pack(self, **kwargs):
        self.root.pack(kwargs)
        
        
        
        
class OperationInput:
    def __init__(self, parent, name):
        self.root = ttk.Frame(parent)
        tk.Label(self.root, text=name).pack()
        self.input = ScrollTextDisplay(self.root, disabled=False, height=10, width=90)
        self.input.pack()
        
    def read(self):
        return self.input.read()
        
    def pack(self, **kwargs):
        self.root.pack(kwargs)
        
    def unpack(self):
        self.root.pack_forget()
        






