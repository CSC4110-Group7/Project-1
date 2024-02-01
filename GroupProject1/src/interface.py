from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from manageFrame import ManageFrame
from queryFrame import getQueryFrame
from infoFrame import InfoFrame

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
interface.addTab(InfoFrame(interface.root).root, "info")
interface.addTab(ManageFrame(interface.root).root, "manage")
interface.addTab(getQueryFrame(interface.root), "query")
interface.mainloop()
