import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://localhost:8000"

# Funciones para la API
def create_user():
    contrato = contrato_entry.get()
    nombre = nombre_entry.get()
    apellidos = apellidos_entry.get()
    direccion = direccion_entry.get()
    user_data = {
        "contrato": contrato,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion
    }
    response = requests.post(f"{API_URL}/usuarios/", json=user_data)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Usuario creado exitosamente")
        get_users()
    else:
        messagebox.showerror("Error", response.json().get("detail", "Error desconocido"))

def get_users():
    response = requests.get(f"{API_URL}/usuarios/")
    if response.status_code == 200:
        users = response.json()
        user_list.delete(*user_list.get_children())
        for user in users:
            user_list.insert("", "end", values=(user["contrato"], user["nombre"], user["apellidos"], user["direccion"]))
    else:
        messagebox.showerror("Error", response.json().get("detail", "Error desconocido"))

def get_user():
    contrato = contrato_entry.get()
    response = requests.get(f"{API_URL}/usuarios/{contrato}")
    if response.status_code == 200:
        user = response.json()
        nombre_entry.delete(0, tk.END)
        apellidos_entry.delete(0, tk.END)
        direccion_entry.delete(0, tk.END)
        nombre_entry.insert(0, user["nombre"])
        apellidos_entry.insert(0, user["apellidos"])
        direccion_entry.insert(0, user["direccion"])
    else:
        messagebox.showerror("Error", response.json().get("detail", "Error desconocido"))

def update_user():
    contrato = contrato_entry.get()
    nombre = nombre_entry.get()
    apellidos = apellidos_entry.get()
    direccion = direccion_entry.get()
    user_data = {
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion
    }
    response = requests.put(f"{API_URL}/usuarios/{contrato}", json=user_data)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Usuario actualizado exitosamente")
        get_users()
    else:
        messagebox.showerror("Error", response.json().get("detail", "Error desconocido"))

def delete_user():
    contrato = contrato_entry.get()
    response = requests.delete(f"{API_URL}/usuarios/{contrato}")
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
        get_users()
    else:
        messagebox.showerror("Error", response.json().get("detail", "Error desconocido"))

# Configuración de la interfaz
root = tk.Tk()
root.title("Gestión de Usuarios del Acueducto")

# Frame para el formulario
form_frame = ttk.Frame(root, padding="10")
form_frame.grid(row=0, column=0, sticky=tk.W)

ttk.Label(form_frame, text="Contrato:").grid(row=0, column=0, sticky=tk.W)
contrato_entry = ttk.Entry(form_frame, width=20)
contrato_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, sticky=tk.W)
nombre_entry = ttk.Entry(form_frame, width=20)
nombre_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(form_frame, text="Apellidos:").grid(row=2, column=0, sticky=tk.W)
apellidos_entry = ttk.Entry(form_frame, width=20)
apellidos_entry.grid(row=2, column=1, sticky=tk.W)

ttk.Label(form_frame, text="Dirección:").grid(row=3, column=0, sticky=tk.W)
direccion_entry = ttk.Entry(form_frame, width=20)
direccion_entry.grid(row=3, column=1, sticky=tk.W)

# Frame para los botones
button_frame = ttk.Frame(root, padding="10")
button_frame.grid(row=1, column=0, sticky=tk.W)

ttk.Button(button_frame, text="Crear Usuario", command=create_user).grid(row=0, column=0, sticky=tk.W)
ttk.Button(button_frame, text="Consultar Usuario", command=get_user).grid(row=0, column=1, sticky=tk.W)
ttk.Button(button_frame, text="Actualizar Usuario", command=update_user).grid(row=0, column=2, sticky=tk.W)
ttk.Button(button_frame, text="Eliminar Usuario", command=delete_user).grid(row=0, column=3, sticky=tk.W)

# Frame para la lista de usuarios
list_frame = ttk.Frame(root, padding="10")
list_frame.grid(row=2, column=0, sticky=tk.W)

columns = ("contrato", "nombre", "apellidos", "direccion")
user_list = ttk.Treeview(list_frame, columns=columns, show="headings")
for col in columns:
    user_list.heading(col, text=col)
    user_list.column(col, width=100)
user_list.pack()

ttk.Button(list_frame, text="Refrescar Lista", command=get_users).pack()

# Iniciar la aplicación
get_users()
root.mainloop()
