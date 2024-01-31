from tkinter import *
from tkinter import ttk
from licenseFrame import getLicenseFrame
from manageFrame import getManageFrame
from queryFrame import getQueryFrame
from infoFrame import getInfoFrame

window = Tk();
window.title("ForestDB");

main_frame = ttk.Frame(window)

tabs = {}
currentTab = 'license'

tab_frame = ttk.Frame(main_frame)

def addTab(name, frame):
    tabs[name] = frame
    ttk.Button(master=tab_frame, text=name, command=lambda: setCurrentTab(name)).pack(side=LEFT)

def tabButtonHandler(evt):
    setCurrentTab(evt.widget.text)

def setCurrentTab(name):
    global currentTab
    if(currentTab == 'license'):
        license_frame.pack_forget()
    else:
        tabs[currentTab].pack_forget()
    tabs[name].pack()
    currentTab = name

addTab('manage', getManageFrame(main_frame=main_frame))
addTab('query', getQueryFrame(main_frame=main_frame))
addTab('info', getInfoFrame(main_frame=main_frame))

def reloadQueryTab():
    tabs['query'] = getQueryFrame(main_frame=main_frame)


def licenseAgreementButton():
    main_frame.pack()
    tab_frame.pack(side=TOP)
    setCurrentTab('manage')

license_frame = getLicenseFrame(window, licenseAgreementButton)
license_frame.pack()



window.mainloop();