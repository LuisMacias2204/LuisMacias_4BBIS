from products import Producto
from exceptions import ProductoNoEncontrado


class Inventario:
    def __init__(self):
        self.productos = {
            "A001": Producto("A001", "Laptop", 10),
            "B002": Producto("B002", "Mouse", 25),
            "C003": Producto("C003", "Teclado", 15),
            "D004": Producto("D004", "Monitor", 8),
        }

    def retirar(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(
                f"El producto con código '{codigo}' no existe."
            )

        return self.productos[codigo].retirar(cantidad)
