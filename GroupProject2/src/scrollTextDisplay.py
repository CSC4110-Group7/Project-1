import tkinter as tk
from tkinter import ttk

class ScrollTextDisplay:
    def __init__(self, parent, **kwargs):
        should_wrap_text = kwargs.pop('wrap', tk.WORD)
        should_disable = kwargs.pop('disabled', True)
        should_height = kwargs.pop('height', 0)
        should_width = kwargs.pop('width', 0)
        self.text_content = kwargs.pop('text', "")
        self.parent = parent

        self.root = ttk.Frame(self.parent)

        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textbox = tk.Text(self.root, wrap=should_wrap_text)
        if(should_height):
            self.textbox.config(height=should_height)
        if(should_width):
            self.textbox.config(width=should_width)
        
        self.textbox.insert(tk.END, self.text_content)
        if(should_disable):
            self.textbox.config(state=tk.DISABLED)
        self.textbox.pack(side=tk.LEFT)
        
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        
    def insert(self, text, start=tk.END):
        self.textbox.insert(start, text)
        
    def read(self, start="1.0", end=tk.END):
        return self.textbox.get(start, end)

    def clear(self, start=0, end=tk.END):
        self.textbox.delete(start, end)

    def pack(self, **kwargs):
        self.root.pack(kwargs)
        
        
class ScrollListDisplay:
    def __init__(self, parent, **kwargs):
        self.text_content = kwargs.pop('text', "")
        self.parent = parent

        self.root = ttk.Frame(self.parent)

        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textbox = tk.Listbox(self.root, font="TkFixedFont")
        self.textbox.insert(tk.END, self.text_content)
        self.textbox.pack(fill=tk.X)
        
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        
    def insert(self, text, start=tk.END):
        self.textbox.insert(start, text)

    def clear(self, start=0, end=tk.END):
        self.textbox.delete(start, end)

    def pack(self, **kwargs):
        self.root.pack(kwargs)