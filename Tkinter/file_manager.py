import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os


class FileManager():
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("File manager")
    self.window.geometry("900x600")
    self.window.resizable(False, False)

    self.directory_path = None

    self.files_list = None
    self.preview_list = None
    self.files_scrollbar = None
    self.preview_scrollbar = None
    self.path_label = None
    self.move_files_button = None

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

    self.move_files_button = tk.Button(controls_frame, text="Move files", command=self.move_files)
    self.move_files_button.pack()

    self.path_label = tk.Label(controls_frame, text="Path: ------")
    self.path_label.pack()

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

  def move_files(self):
    classification = {
      "Documents": { ".txt", ".pdf", ".doc", ".docx", ".rtf" },
      "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
      "Video": {".mp4", ".avi", ".mkv", ".mov", ".wmv"},
      "Audio": {".mp3", ".wav", ".flac", ".aac"},
    }

    if self.directory_path:
      directory =  os.listdir(self.directory_path)
      for file in directory:
        file_path = os.path.join(self.directory_path, file)

        # Skip directory
        if os.path.isdir(file_path):
          continue

        name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        # Find the category
        target_category = "Others" # Default category

        for category, extensions in classification.items():
          if file_extension in extensions:
            target_category = category
            break

        # Create target folder and move file
        category_path = os.path.join(self.directory_path, target_category)
        os.makedirs(category_path, exist_ok=True)

        source_path = os.path.join(self.directory_path, file)
        destination_path = os.path.join(category_path, file)

        try:
          shutil.move(source_path, destination_path)
        except Exception as e:
          print(f"Error moving {file}: {e}")

  def show_preview(self, classification):
    if self.preview_list:
      self.preview_list.destroy()
    if self.preview_scrollbar:
      self.preview_scrollbar.destroy()

    # Create frame for preview list
    preview_frame = tk.Frame(self.window)
    preview_frame.grid(row=2, column=1, sticky="nsew", padx=(5, 10), pady=(0, 10))
    preview_frame.grid_columnconfigure(0, weight=1)
    preview_frame.grid_rowconfigure(0, weight=1)

    self.preview_list = tk.Listbox(preview_frame)
    self.preview_scrollbar = tk.Scrollbar(preview_frame)
    self.preview_list.grid(row=0, column=0, sticky="nsew")
    self.preview_scrollbar.grid(row=0, column=1, sticky="ns")

    for folder, files in classification.items():
      if files:
        self.preview_list.insert(tk.END, f"📁 {folder}")
        for file in files:
          self.preview_list.insert(tk.END, f"  - {file}")

  def show_files(self, path):
    if self.files_list:
      self.files_list.destroy()
    if self.files_scrollbar:
      self.files_scrollbar.destroy()

    def show_selection(listbox):
      selection = listbox.curselection()
      if selection:
        index = selection[0]
        file = listbox.get(index)
        print(f"Archivo seleccionado: {file}")

    # Create frames for files list
    files_frame = tk.Frame(self.window)
    files_frame.grid(row=2, column=0, sticky="nsew", padx=(10, 5), pady=(0, 10))

    files_frame.grid_columnconfigure(0, weight=1)
    files_frame.grid_rowconfigure(0, weight=1)

    # Create list with scrollbar
    self.files_list = tk.Listbox(files_frame)
    self.files_scrollbar = tk.Scrollbar(files_frame)

    self.files_list.config(yscrollcommand=self.files_scrollbar.set)
    self.files_scrollbar.config(command=self.files_list.yview)

    self.files_list.grid(row=0, column=0, sticky="nsew")
    self.files_scrollbar.grid(row=0, column=1, sticky="ns")

    # Set list
    try:
      directory = os.listdir(path)

      for file in directory:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
          name, extension = os.path.splitext(file)
          self.files_list.insert(tk.END, f"{name}{extension}")
          self.files_list.bind("<<ListboxSelect>>", lambda e: show_selection(self.files_list))
    except PermissionError:
      messagebox.showerror("Error", "No tienes permisos para listar esta carpeta")

  def select_folder(self):
    self.directory_path = filedialog.askdirectory()
    if self.directory_path:
      self.path_label.config(text=f"Path: {self.directory_path}")
      self.show_files(self.directory_path)
      classification = self.organize_files(self.directory_path)
      self.show_preview(classification)

  def start(self):
    self.window.mainloop()


app = FileManager()
app.start()