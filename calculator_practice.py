from tkinter import *

root = Tk()

frame = Frame(root, width=650, background="gray",  padx=10, pady=10)
frame.pack( padx=10, pady=10)

#----------------------------------- calculator input -----------------------------------#

calculatorInput = Entry(frame)
calculatorInput.grid(row=1,column=1, padx=10, pady=10, columnspan=4)
calculatorInput.config(background="#eaeaea", fg="black", justify="right")

#----------------------------------- calculator buttons -----------------------------------#

number_7 = Button(frame, text="7", width=3)
number_7.grid(row="2",column="1")
number_8 = Button(frame, text="8", width=3)
number_8.grid(row="2", column="2")
number_9 = Button(frame, text="9", width=3)
number_9.grid(row="2", column="3")
divisionButton = Button(frame, text="/", width=3)
divisionButton.grid(row="2", column="4")

number_4 = Button(frame, text="4", width=3)
number_4.grid(row="3",column="1")
number_5 = Button(frame, text="5", width=3)
number_5.grid(row="3", column="2")
number_6 = Button(frame, text="6", width=3)
number_6.grid(row="3", column="3")
multiplicationButton = Button(frame, text="x", width=3)
multiplicationButton.grid(row="3", column="4")

number_1 = Button(frame, text="1", width=3)
number_1.grid(row="4",column="1")
number_2 = Button(frame, text="2", width=3)
number_2.grid(row="4", column="2")
number_3 = Button(frame, text="3", width=3)
number_3.grid(row="4", column="3")
subtractButton = Button(frame, text="-", width=3)
subtractButton.grid(row="4", column="4")

number_0 = Button(frame, text="0", width=3)
number_0.grid(row="5", column="1")
commaButton = Button(frame, text=",", width=3)
commaButton.grid(row="5", column="2")
equalButton = Button(frame, text="=", width=3)
equalButton.grid(row="5", column="3")
sumButton = Button(frame, text="+", width=3)
sumButton.grid(row="5", column="4")
root.mainloop()