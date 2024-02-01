import tkinter as tk
from tkinter import ttk
import os

#Read license content from file
def ReadLicenseFile():
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, 'license.txt')
    with open(filepath, 'r') as file:
        content = ''.join([line.strip() for line in file.readlines()])
    file.close()
    return content

class LicenseConfirmFrame:
    def __init__(self, parent, packAfterAgree):
        self.license_content = ReadLicenseFile()
        self.parent = parent
        self.packAfterAgree = packAfterAgree

        self.root = ttk.Frame(self.parent, padding=10)
        self.title = ttk.Label(self.root, text='User License Agreement').pack()
        self.content_frame = ttk.Frame(self.root, padding=10)

        self.scrollbar = tk.Scrollbar(self.content_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.content = tk.Text(self.content_frame, wrap=tk.WORD)
        self.content.insert(tk.END, self.license_content)
        self.content.pack()

        self.content.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.content.yview)
        self.content_frame.pack()

        self.button_frame = ttk.Frame(self.root)
        self.agree_button = ttk.Button(self.button_frame, text='I Agree', padding=5, command=self.agreementCallback).pack(side=tk.LEFT)
        self.disagree_button = ttk.Button(self.button_frame, text="I Don't Agree", padding=5, command=self.disagreementCallback).pack(side=tk.LEFT)
        self.button_frame.pack()
        self.root.pack()

    def agreementCallback(self):
        self.root.pack_forget()
        self.packAfterAgree()

    def disagreementCallback(self):
        self.parent.destroy()
