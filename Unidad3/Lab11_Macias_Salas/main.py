from inventory import Inventario
from exceptions import ErrorInventario


def main():
    inventario = Inventario()

    codigo = input("Código del producto: ").strip()

    try:
        cantidad = int(input("Cantidad a retirar: "))
        restante = inventario.retirar(codigo, cantidad)

    except ValueError:
        print("Error: la cantidad debe ser un número entero.")

    except ErrorInventario as error:
        print(f"Error de inventario: {error}")

    else:
        print(f"Retiro exitoso. Stock restante: {restante}")


if __name__ == "__main__":
    main()
