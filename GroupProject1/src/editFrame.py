from tkinter import ttk

def getEditFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Edit', padding=20).pack();
    return frame