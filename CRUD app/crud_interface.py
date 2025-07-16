from tkinter import *
from tkinter import messagebox
from DB_Methods import DataBaseManager

root = Tk()
db = DataBaseManager()

def connect_db():
  try:
      created = db.connect_and_init()
      if created:
        messagebox.showinfo("Database", "Database and table created successfully.")
      else:
        messagebox.showinfo("Database", "Table already exists.")
  except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")

def close_app():
  root.destroy()

userId = StringVar()
userName = StringVar()
userLastname = StringVar()
userPassword = StringVar()
userDirection = StringVar()

def clean_entries():
  userId.set("")
  userName.set("")
  userLastname.set("")
  userPassword.set("")
  userDirection.set("")
  commentaryText.delete(1.0, END)

menuNav = Menu(root)
root.config(menu=menuNav, width=300, height=300)

#------------- DB Menu -------------#
dbMenu = Menu(menuNav, tearoff=0)
dbMenu.add_command(label="Connect", command=connect_db)
dbMenu.add_command(label="Exit", command=close_app)

menuNav.add_cascade(label="DB", menu=dbMenu)

deleteMenu = Menu(menuNav, tearoff=0)
deleteMenu.add_command(label="Delete entries", command=clean_entries)

menuNav.add_cascade(label="Delete", menu=deleteMenu)
#------------- CRUD Menu -------------#
crudMenu = Menu(menuNav, tearoff=0)
crudMenu.add_command(label="Create")
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

menuNav.add_cascade(label="Crud", menu=crudMenu)


#------------- Inputs frame and entries -------------#
inputsFrame = Frame(root)
inputsFrame.pack()

idInput = Entry(inputsFrame, textvariable=userId)
idInput.grid(row=0, column=1, padx=10, pady=10)

nameInput = Entry(inputsFrame, textvariable=userName)
nameInput.grid(row=1, column=1, padx=10, pady=10)

passwordInput = Entry(inputsFrame, textvariable=userPassword)
passwordInput.grid(row=2, column=1, padx=10, pady=10)
passwordInput.config(show="*") # Show * instead of text

lastnameInput = Entry(inputsFrame, textvariable=userLastname)
lastnameInput.grid(row=3, column=1, padx=10, pady=10)

directionInput = Entry(inputsFrame, textvariable=userDirection)
directionInput.grid(row=4, column=1, padx=10, pady=10)

commentaryText = Text(inputsFrame, width=16, height=5)
commentaryText.grid(row=5, column=1)
scrollVert = Scrollbar(inputsFrame, command=commentaryText.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

commentaryText.config(yscrollcommand=scrollVert.set)

#------------- Inputs labels -------------#
idLabel = Label(inputsFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nameLabel = Label(inputsFrame, text="Name:")
nameLabel.grid(row=1, column=0,  sticky="e", padx=10, pady=10)
passLabel = Label(inputsFrame, text="Password:")
passLabel.grid(row=2, column=0,  sticky="e", padx=10, pady=10)
lastnameLabel =  Label(inputsFrame, text="Last name:")
lastnameLabel.grid(row=3, column=0,  sticky="e", padx=10, pady=10)
directionLabel =  Label(inputsFrame, text="Direction:")
directionLabel.grid(row=4, column=0,  sticky="e", padx=10, pady=10)
commentLabel =  Label(inputsFrame, text="Comment:")
commentLabel.grid(row=5, column=0,  sticky="e", padx=10, pady=10)

#------------- Crud buttons -------------#
buttonsFrame = Frame(root)
buttonsFrame.pack()

createButton = Button(buttonsFrame, text="Create")
createButton.grid(row=1, column=0, sticky="e", padx=10, pady=10)
readButton = Button(buttonsFrame, text="Read")
readButton.grid(row=1, column=1, sticky="e", padx=10, pady=10)
updateButton = Button(buttonsFrame, text="Update")
updateButton.grid(row=1, column=2, sticky="e", padx=10, pady=10)
deleteButton = Button(buttonsFrame, text="Delete")
deleteButton.grid(row=1, column=3, sticky="e", padx=10, pady=10)


#----------------------------------------#
root.mainloop()