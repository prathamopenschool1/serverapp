#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from collections import OrderedDict
from tkinter import ttk  
import os
import sys


def stop_kolibri():
        try:
                os.system('sudo kolibri stop')
                messagebox.showinfo("SERVERAPP", "kolibri server stopped")
        except Exception as e:
                messagebox.showinfo("SERVERAPP", e)

def start_kolibri():
        try:
                os.system('sudo kolibri start')
                messagebox.showinfo("SERVERAPP", "kolibri server started")
        except Exception as e:
                messagebox.showinfo("SERVERAPP", e)

def start_hotspot():
        try:
                os.system('sudo systemctl hostapd stop')
                os.system('sudo systemctl hostapd start')
                os.system('sudo service networking restart')
                os.system('sudo reboot')
        except Exception as e:
                messagebox.showinfo("SERVERAPP", e)
	

window = Tk()

window.wm_title("SERVERAPP")

#window.geometry("300x100")

window.resizable(0, 0)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

stop = Button(window,text="STOP KOLIBRI", width=15,command=stop_kolibri)
stop.grid(row=1, column=0)

start = Button(window,text="START KOLIBRI", width=15,command=start_kolibri)
start.grid(row=1, column=1)

hotspot = Button(window,text="START WIFI", width=15, command=start_hotspot)
hotspot.grid(row=2, column=0)

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))
#window.geometry("350x100")

window.mainloop()
