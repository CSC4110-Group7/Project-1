from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from manageFrame import getManageFrame
from queryFrame import getQueryFrame
from infoFrame import getInfoFrame

class MainInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("ForestDB")
        self.root.geometry("800x500")

        self.tab_control = ttk.Notebook(self.root)
        self.license = LicenseConfirmFrame(self.root, self.packAfterAgree)
        self.license.pack()
        # self.tab_control.pack(expand=1, fill="both")

    def addTab(self, frame, label):
        self.tab_control.add(frame, text=label)

    def packAfterAgree(self):
        self.tab_control.pack(expand=1, fill="both")

    def mainloop(self):
        self.root.mainloop()

interface = MainInterface()
interface.addTab(getInfoFrame(interface.root), "info")
interface.addTab(getManageFrame(interface.root), "manage")
interface.addTab(getQueryFrame(interface.root), "query")
interface.mainloop()
