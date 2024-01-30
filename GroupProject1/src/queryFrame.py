from tkinter import ttk

def getQueryFrame(main_frame):
    frame = ttk.Frame(master=main_frame)
    ttk.Label(master=frame, text='Query', padding=20).pack();
    return frame