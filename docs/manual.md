# Manual de Usuario - Sistema de Inventario

Este manual describe el funcionamiento y uso de la aplicación de gestión de inventarios.

## 1. Requisitos Previos
* Tener instalado **Python 3.x**.
* Acceso a una terminal o consola de comandos.

## 2. Inicio de la Aplicación
Para iniciar el programa, navega hasta la carpeta raíz del proyecto y ejecuta:
```bash
python src/main.py 

Guía de Opciones del Menú

A. Agregar Producto

1.Selecciona la Opción 1.

2.Ingresa el nombre del producto (ej. "Teclado").

3.Ingresa la cantidad inicial en stock (debe ser un número entero).

4.Ingresa el precio unitario (admite decimales).


B. Actualizar Stock

1.Selecciona la Opción 2.

2.Escribe el nombre exacto del producto que deseas modificar.

3.Ingresa la nueva cantidad total.

C. Eliminar Producto

1.Selecciona la Opción 3.

2.Escribe el nombre del producto que deseas quitar del sistema.
Nota: Esta acción no se puede deshacer.

D. Mostrar Inventario

1.Selecciona la Opción 4.

2.El sistema imprimirá una tabla con todos los productos registrados, sus cantidades y precios.

Solución de Problemas

Error de Valor (ValueError): Asegúrate de no usar letras en los campos de "Cantidad" o "Precio".

Producto no encontrado: Verifica que el nombre esté bien escrito. El sistema no distingue entre mayúsculas y minúsculas.
