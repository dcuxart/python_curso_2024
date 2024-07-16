from libros import GestionLibros
from prestamos import GestionPrestamos
from usuarios import GestionUsuarios


def menuPrincipal(gestionLibros, gestionUsuarios, gestionPrestamos):
    while True:
        print("---Gestión de una biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción")

        if opcion == "1":
            # Llama a función menu_libros de otro módulo
            gestionLibros.menu_libros()
            print("opt 1")

        elif opcion == "2":
            # Llama a función menu_usuarios de otro módulo
            gestionUsuarios.menu_usuarios()
            print("opt 2")

        elif opcion == "3":
            # Llama a función menu_prestamos de otro módulo
            gestionPrestamos.menuPrestamos()
            print("opt 3")

        elif opcion == "4":
            print("Gracias por utilizar nuestra app")
            break

        else:
            print("Opción no válida. Vuelve a intentarlo")

# Intancias:
gestionLibros = GestionLibros()
gestionUsuarios = GestionUsuarios()
gestionPrestamos = GestionPrestamos(gestionLibros, gestionUsuarios)
# Carga el menú principal
menuPrincipal(gestionLibros)
# menuPrincipal(gestionPrestamos)