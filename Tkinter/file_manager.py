import tkinter as tk
from tkinter import filedialog, messagebox
import os

window = tk.Tk()
window.title("File manager")
window.geometry("400x300")
window.resizable(False, False)

def select_folder():
  path = filedialog.askdirectory()
  print(path)

  path_label.config(text=f"Path: {path}")

select_folder_label = tk.Label(window, text="Select folder")
select_folder_label.pack()
select_folder_button = tk.Button(window, text="Select", command=select_folder)
select_folder_button.pack()

path_label = tk.Label(window, text="Path: ------")
path_label.pack()

window.mainloop()