from inventory import Inventario

def menu():
    mi_inventario = Inventario()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario: "))
                mi_inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("Error: Cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            try:
                nueva_cantidad = int(input("Nueva cantidad total: "))
                mi_inventario.actualizar_stock(nombre, nueva_cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            mi_inventario.eliminar_producto(nombre)

        elif opcion == "4":
            mi_inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
