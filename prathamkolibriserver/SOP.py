#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import socket
import errno
import os
import sys


def stop_kolibri():
    try:
        os.system('sudo kolibri stop')
        messagebox.showinfo("SERVERAPP", "kolibri server stopped")
    except Exception as stp:
        messagebox.showinfo("SERVERAPP", stp)


def start_kolibri():
    try:
        os.system('sudo kolibri start')
        messagebox.showinfo("SERVERAPP", "kolibri server started")
    except Exception as st:
        messagebox.showinfo("SERVERAPP", st)


window = Tk()

window.wm_title("SERVERAPP")

window.resizable(0, 0)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

start = Button(window, text="START KOLIBRI", width=15, command=start_kolibri)
start.grid(row=2, column=0)

stop = Button(window, text="STOP KOLIBRI", width=15, command=stop_kolibri)
stop.grid(row=2, column=1)

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))
# window.geometry("350x100")

window.mainloop()
