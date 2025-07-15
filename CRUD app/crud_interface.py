from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

menuNav = Menu(root)
root.config(menu=menuNav, width=300, height=300)

#------------- DB Menu -------------#
dbMenu = Menu(menuNav, tearoff=0)
dbMenu.add_command(label="Connect")
dbMenu.add_command(label="Exit")

menuNav.add_cascade(label="DB", menu=dbMenu)

deleteMenu = Menu(menuNav, tearoff=0)
deleteMenu.add_command(label="Delete entries")

menuNav.add_cascade(label="Delete", menu=deleteMenu)
#------------- CRUD Menu -------------#
crudMenu = Menu(menuNav, tearoff=0)
crudMenu.add_command(label="Create")
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

menuNav.add_cascade(label="Crud", menu=crudMenu)


#------------- Inputs frame -------------#
inputsFrame = Frame(root)
inputsFrame.pack()

idInput = Entry(inputsFrame)
idInput.grid(row=0, column=1, padx=10, pady=10)
nameInput = Entry(inputsFrame)
nameInput.grid(row=1, column=1, padx=10, pady=10)
passwordInput = Entry(inputsFrame)
passwordInput.grid(row=2, column=1, padx=10, pady=10)
passwordInput.config(show="*") # Show * instead of text
lastnameInput = Entry(inputsFrame)
lastnameInput.grid(row=3, column=1, padx=10, pady=10)
directionInput = Entry(inputsFrame)
directionInput.grid(row=4, column=1, padx=10, pady=10)

commentaryText = Text(inputsFrame, width=16, height=5)
commentaryText.grid(row=5, column=1)
scrollVert = Scrollbar(inputsFrame, command=commentaryText.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

commentaryText.config(yscrollcommand=scrollVert.set)

root.mainloop()