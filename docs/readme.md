Sistema de Inventario Básico

Este es un proyecto académico desarrollado para la gestión eficiente de productos, permitiendo controlar atributos clave como nombre, cantidad y precio. Está diseñado siguiendo principios de programación orientada a objetos (POO) y metodologías ágiles.

Características

Agregar Productos: Registro de nuevos artículos en el sistema.

Actualizar Stock: Modificación dinámica de las cantidades disponibles.

Eliminar Productos: Limpieza del inventario de forma selectiva.

Visualización: Reporte en consola del estado actual de los productos.

Pruebas Unitarias: Validación automatizada de la lógica de negocio.

Estructura del Proyecto

PROYECTO-4-SISTEMA-DE-INVENTARIO-B-SICO/
├── docs/           # Documentación adicional y manuales.
├── src/            # Código fuente del sistema.
    |__utils/
    |   |_validaciones.py
│   ├── inventory.py  # Lógica de las clases Producto e Inventario.
│   └── main.py       # Interfaz de usuario (Menú interactivo).
├── tests/          # Pruebas automatizadas.
│   └── test_basico.py
└── .gitignore      # Archivos excluidos de Git.

Instalación y Uso

Clonar el repositorio:

git clone https://github.com/Nagisa18/Proyecto-4-Sistema-de-Inventario-B-sico.git
cd Proyecto-4-Sistema-de-Inventario-B-sico

Ejecutar la aplicación:

python src/main.py

Ejecutar las pruebas:

python tests/test_basico.py

Tecnologías Utilizadas

Lenguaje: Python 3.x

Gestión de Versiones: Git & GitHub

Metodología: Kanban (GitHub Projects)