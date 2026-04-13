import tkinter as tk
from tkinter import messagebox
from inventory import Inventario

class AppInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")

        self.inventario = Inventario()

        # --- Inputs ---
        tk.Label(root, text="Nombre").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(root, text="Cantidad").grid(row=1, column=0)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=1, column=1)

        tk.Label(root, text="Precio").grid(row=2, column=0)
        self.entry_precio = tk.Entry(root)
        self.entry_precio.grid(row=2, column=1)

        # --- Botones ---
        tk.Button(root, text="Agregar", command=self.agregar).grid(row=3, column=0)
        tk.Button(root, text="Actualizar", command=self.actualizar).grid(row=3, column=1)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=4, column=0)
        tk.Button(root, text="Mostrar", command=self.mostrar).grid(row=4, column=1)

        # --- Lista ---
        self.lista = tk.Listbox(root, width=60)
        self.lista.grid(row=5, column=0, columnspan=2)

    # --- Funciones ---
    def agregar(self):
        try:
            nombre = self.entry_nombre.get()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())

            self.inventario.agregar_producto(nombre, cantidad, precio)
            messagebox.showinfo("Éxito", "Producto agregado")
            self.mostrar()

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos")

    def actualizar(self):
        try:
            nombre = self.entry_nombre.get()
            cantidad = int(self.entry_cantidad.get())

            self.inventario.actualizar_stock(nombre, cantidad)
            messagebox.showinfo("Éxito", "Stock actualizado")
            self.mostrar()

        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")

    def eliminar(self):
        nombre = self.entry_nombre.get()
        self.inventario.eliminar_producto(nombre)
        messagebox.showinfo("Éxito", "Producto eliminado")
        self.mostrar()

    def mostrar(self):
        self.lista.delete(0, tk.END)
        for producto in self.inventario.productos:
            self.lista.insert(tk.END, str(producto))


# --- Ejecutar app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AppInventario(root)
    root.mainloop()