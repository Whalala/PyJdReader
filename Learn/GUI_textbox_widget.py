import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title = "GUI with button"


enb = False


def click_me():
    action.configure(text="Hello " + name.get())
    action.configure(state='disabled')



ttk.Label(win, text="Enter name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=20, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=1)

name_entered.focus()

win.mainloop()
