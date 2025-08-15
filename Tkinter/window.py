import tkinter as tk

def greet():
  name = entry_name.get()
  if name:
    tag_greet.config(text=f"¡Hello, {name}!")
  else:
    tag_greet.config(text="Please enter a name.")

# Crear la ventana principal
window = tk.Tk()
window.title("My first app")
window.geometry("400x300")
window.resizable(True, True)

# Crear widgets
tag_title = tk.Label(window, text="¿What is you'r name?", font=("Arial", 14))
entry_name = tk.Entry(window, font=("Arial", 12))
button_greet = tk.Button(window, text="Greet", command=greet, bg="lightblue")
tag_greet = tk.Label(window, text="", font=("Arial",12), fg="green")

# Posicionar widgets usando pack
tag_title.pack(pady=10)
entry_name.pack(pady=5)
button_greet.pack(pady=10)
tag_greet.pack(pady=5)

# Iniciar el bucle principal de la aplicación
window.mainloop()