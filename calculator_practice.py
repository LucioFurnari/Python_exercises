from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

#----------------------------------- calculator input -----------------------------------#

calculatorInput = Entry(frame)
calculatorInput.grid(row=1,column=1, padx=10, pady=10, columnspan=4)
calculatorInput.config(background="#eaeaea", fg="black", justify="right", width=40)

#----------------------------------- calculator buttons -----------------------------------#

number_7 = Button(frame, text="7", width=3)
number_7.grid(row="2",column="1")
number_8 = Button(frame, text="8", width=3)
number_8.grid(row="2", column="2")
number_9 = Button(frame, text="9", width=3)
number_9.grid(row="2", column="3")
multiplicationButton = Button(frame, text="x", width=3)
multiplicationButton.grid(row="2", column="4")

root.mainloop()