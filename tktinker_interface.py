from tkinter import *

root = Tk()
root.title("Test window")
# root.resizable(False,False)

root.config(background="#57bdff")

newFrame = Frame(root, width=650, height=450)
newFrame.pack()
newFrame.config(background="#ff8c57")

newLabel = Label(newFrame, text="Hello, this is a label in python", background="#ff8c57")
newLabel.place(x=100,y=200)
newLabel.grid(row=1, column=1)

nameLabel = Label(newFrame, text="Name:")
nameLabel.grid(row=0, column=0)

inputName = Entry(newFrame)
inputName.grid(row=0, column=1)

root.mainloop()