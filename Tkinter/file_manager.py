import tkinter as tk
from tkinter import filedialog, messagebox
import os


class FileManager():
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("File manager")
    self.window.geometry("900x600")
    self. window.resizable(False, False)

    self.files_list = None
    self.preview_list = None
    self.files_scrollbar = None
    self.preview_scrollbar = None

    self.setup_ui()

  def setup_ui(self):
    self.window.grid_columnconfigure(0, weight=1)
    self.window.grid_columnconfigure(1, weight=1)
    self.window.grid_rowconfigure(2, weight=1)

    controls_frame = tk.Frame(self.window)
    controls_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    select_folder_label = tk.Label(controls_frame, text="Select folder")
    select_folder_label.pack()

    select_folder_button = tk.Button(controls_frame, text="Select", command=self.select_folder)
    select_folder_button.pack()

    title_files = tk.Label(self.window, text="Files in Folder", font=("Arial", 12, "bold"))
    title_files.grid(
      row=1, column=0, pady=(10, 5), sticky="w", padx=10
    )
    title_preview = tk.Label(self.window, text="Classification Preview", font=("Arial", 12, "bold"))
    title_preview.grid(
      row=1, column=1, pady=(10,5), sticky="w", padx=10
    )

  def organize_files(self, folder_path):
    classification = {
      "Documents": [],
      "Images": [],
      "Video": [],
      "Audio": [],
      "Others": []
    }

    directory = os.listdir(folder_path)

    for file in directory:
      file_path = os.path.join(folder_path, file)

      if os.path.isfile(file_path):
        name, extension = os.path.splitext(file)
        ext_lower = extension.lower()

        if ext_lower in [".txt", ".pdf", ".doc", ".docx", ".rtf"]:
          classification["Documents"].append(file)
        elif ext_lower in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
          classification["Images"].append(file)
        elif ext_lower in [".mp4", ".avi", ".mkv", ".mov", ".wmv"]:
          classification["Videos"].append(file)
        elif ext_lower in [".mp3", ".wav", ".flac", ".aac"]:
          classification["Audio"].append(file)
        else:
          classification["Others"].append(file)

    return classification


  def start(self):
    self.window.mainloop()

# window = tk.Tk()
# window.title("File manager")
# window.geometry("900x600")
# window.resizable(False, False)

# def organize_files(folder):
#   classification = {
#     "Documents": [],
#     "Images": [],
#     "Videos": [],
#     "Others": []
#   }

#   for file in folder:
#     name, extension = os.path.splitext(file)
#     print(file)
#     if extension in [".txt", ".pdf"]:
#       classification["Documents"].append(file)

#   return classification


# def show_preview(classification):

#   preview_list = tk.Listbox(window)
#   preview_list.grid(row=0, column=1)

#   for folder, files in classification.items():
#     if files:
#       print(f"📁 {folder}")
#       preview_list.insert(tk.END, f"📁 {folder}")
#       for file in files:
#         print(f"  - {file}")
#         preview_list.insert(tk.END, f"  - {file}")

# def select_folder():
#   path = filedialog.askdirectory()

#   path_label.config(text=f"Path: {path}")

#   show_files(path)
#   directory = os.listdir(path)
#   classification = organize_files(directory)
#   show_preview(classification)

# def show_selection(listbox):
#   selection = listbox.curselection()
#   if selection:
#     index = selection[0]
#     file = listbox.get(index)

# def show_files(path):
#   directory = os.listdir(path)

#   list = tk.Listbox(window)
#   scrollbar = tk.Scrollbar(window)

#   list.config(yscrollcommand=scrollbar.set)
#   scrollbar.config(command=list.yview)

#   list.pack(side="left", fill="both", expand=True)
#   scrollbar.pack(side="right", fill="y")

#   for file in directory:
#     name, extension = os.path.splitext(file)
#     file_path = os.path.join(path, file)

#     if os.path.isfile(file_path):
#       list.insert(tk.END, f"{name}{extension}")
#       list.bind("<<ListboxSelect>>", lambda e: show_selection(list))


# select_folder_label = tk.Label(window, text="Select folder")
# select_folder_label.pack()
# select_folder_button = tk.Button(window, text="Select", command=select_folder)
# select_folder_button.pack()

# path_label = tk.Label(window, text="Path: ------")
# path_label.pack()

# window.mainloop()