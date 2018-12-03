import tkinter as tk
from tkinter import  ttk


win = tk.Tk()

win.title ="GUI with button"

a_label = ttk.Label(win, text="ALabel")
a_label.grid(column=0, row=0)



def click_me():
    action.configure(text="** I have been Clicked.**")
    a_label.configure(foreground='red', text="Red Label!")
    #a_label.configure(text="A Red Label")

action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=0)
win.mainloop()
