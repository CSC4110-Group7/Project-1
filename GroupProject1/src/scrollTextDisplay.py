import tkinter as tk
from tkinter import ttk

class ScrollTextDisplay:
    def __init__(self, parent, **kwargs):
        should_wrap_text = kwargs.pop('wrap', tk.WORD)
        self.text_content = kwargs.pop('text', "")
        self.parent = parent

        self.root = ttk.Frame(self.parent)

        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textbox = tk.Text(self.root, wrap=should_wrap_text)
        self.textbox.insert(tk.END, self.text_content)
        self.textbox.pack()
        
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        
    def insert(self, text, start=tk.END):
        self.textbox.insert(start, text)

    def clear(self, start=0, end=tk.END):
        self.delete(start, end)

    def pack(self, **kwargs):
        self.root.pack(kwargs)