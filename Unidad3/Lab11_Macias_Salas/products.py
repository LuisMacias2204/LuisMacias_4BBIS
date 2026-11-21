from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise CantidadInvalida("La cantidad debe ser un número entero.")

        if cantidad <= 0:
            raise CantidadInvalida("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise StockInsuficiente(
                f"Stock insuficiente de '{self.nombre}': "
                f"solicitado {cantidad}, disponible {self.stock}."
            )

        self.stock -= cantidad
        return self.stock
