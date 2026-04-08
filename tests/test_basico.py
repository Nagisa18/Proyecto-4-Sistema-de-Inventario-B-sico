import unittest
import sys
import os

# Esto permite que el test encuentre la carpeta 'src' para importar el inventario
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from inventory import Inventario

class TestInventario(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba: crea un inventario limpio"""
        self.repo = Inventario()

    def test_agregar_producto(self):
        """Prueba que un producto se agregue correctamente"""
        self.repo.agregar_producto("Manzana", 10, 500.0)
        self.assertEqual(len(self.repo.productos), 1)
        self.assertEqual(self.repo.productos[0].nombre, "Manzana")

    def test_actualizar_stock(self):
        """Prueba que el stock cambie correctamente"""
        self.repo.agregar_producto("Arroz", 50, 1500.0)
        self.repo.actualizar_stock("Arroz", 30)
        self.assertEqual(self.repo.productos[0].cantidad, 30)

    def test_eliminar_producto(self):
        """Prueba que el producto desaparezca de la lista"""
        self.repo.agregar_producto("Aceite", 5, 8000.0)
        self.repo.eliminar_producto("Aceite")
        self.assertEqual(len(self.repo.productos), 0)

if __name__ == '__main__':
    unittest.main()
