from tkinter import *

root = Tk()
root.title("Test window")
# root.resizable(False,False)

root.config(background="#57bdff")

newFrame = Frame()
newFrame.pack()
newFrame.config(width=650, height=450)
newFrame.config(background="#ff8c57")
root.mainloop()