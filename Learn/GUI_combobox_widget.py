import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title = "GUI with button"


enb = False


def click_me():
    action.configure(text="Hello " + name.get() + number.get())
    #action.configure(state='disabled')



ttk.Label(win, text="Enter name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=20, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1)


ttk.Label(win, text="Choosee a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


name_entered.focus()

win.mainloop()
