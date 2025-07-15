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

root.mainloop()