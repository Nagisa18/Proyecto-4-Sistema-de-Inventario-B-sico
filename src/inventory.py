class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre:15} | Stock: {self.cantidad:5} | Precio: ${self.precio:8.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print(f" Producto '{nombre}' agregado con éxito.")

    def actualizar_stock(self, nombre, nueva_cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                producto.cantidad = nueva_cantidad
                print(f" Stock de '{nombre}' actualizado a {nueva_cantidad}.")
                return
        print(f" Error: No se encontró el producto '{nombre}'.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                print(f" Producto '{nombre}' eliminado del inventario.")
                return
        print(f" Error: No se pudo eliminar. '{nombre}' no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Estado Actual del Inventario ---")
            for p in self.productos:
                print(p)
            print("------------------------------------\n")


# --- Bloque de prueba ---
if __name__ == "__main__":
    mi_repo = Inventario()
    
    mi_repo.agregar_producto("Arroz", 50, 1500.0)
    mi_repo.agregar_producto("Aceite", 10, 8500.0)
    
    mi_repo.mostrar_inventario()
    
    mi_repo.actualizar_stock("Arroz", 45)
    
    mi_repo.eliminar_producto("Aceite")
    
    mi_repo.mostrar_inventario()