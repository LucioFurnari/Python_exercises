import tkinter as tk
from tkinter import filedialog, messagebox
import os

window = tk.Tk()
window.title("File manager")
window.geometry("900x600")
window.resizable(False, False)

def select_folder():
  path = filedialog.askdirectory()

  path_label.config(text=f"Path: {path}")

  show_files(path)

def show_selection(listbox):
  selection = listbox.curselection()
  if selection:
    index = selection[0]
    file = listbox.get(index)
    print(f"You selected: {file}")

def show_files(path):
  directory = os.listdir(path)

  list = tk.Listbox(window)
  scrollbar = tk.Scrollbar(window)

  list.config(yscrollcommand=scrollbar.set)
  scrollbar.config(command=list.yview)

  list.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")

  for file in directory:
    name, extension = os.path.splitext(file)
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
      print(file)
      list.insert(tk.END, f"{name}{extension}")
      list.bind("<<ListboxSelect>>", lambda e: show_selection(list))


select_folder_label = tk.Label(window, text="Select folder")
select_folder_label.pack()
select_folder_button = tk.Button(window, text="Select", command=select_folder)
select_folder_button.pack()

path_label = tk.Label(window, text="Path: ------")
path_label.pack()

window.mainloop()