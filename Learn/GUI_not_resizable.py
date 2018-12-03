import tkinter as tk

win = tk.Tk()

win.title("No resizable GUI")

win.resizable(False, True)#Width can not be changed while you can resize the Height

win.mainloop()