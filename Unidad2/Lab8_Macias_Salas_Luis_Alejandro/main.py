import tkinter as tk

from models.conexion import Conexion
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.authentication import Authentication


def probar_conexion():
    """Verifica la conexión con MySQL antes de abrir la aplicación."""
    conexion = Conexion().conectar()

    if conexion is None:
        print("No se pudo conectar a la base de datos 'login_mvc'.")
        print("Verifica que MySQL esté encendido y que hayas ejecutado "
              "database.sql.")
        return False

    print("Conexión con MySQL exitosa.")
    conexion.close()
    return True


def main():
    probar_conexion()

    root = tk.Tk()

    modelo = UserModel()
    vista = LoginView(root)
    Authentication(modelo, vista)

    root.mainloop()


if __name__ == "__main__":
    main()