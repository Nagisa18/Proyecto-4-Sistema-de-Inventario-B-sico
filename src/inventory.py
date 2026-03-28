class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} | Stock: {self.cantidad} | Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado con éxito.")