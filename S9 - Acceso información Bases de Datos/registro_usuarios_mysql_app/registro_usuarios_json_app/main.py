from libros import GestionLibros
from usuarios import GestionUsuarios
from prestamos import GestionPrestamos


def menu_principal(gestion_libros, gestion_usuarios, gestion_prestamos):
    while True:
        print("---Gestión de una biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción")

        if opcion == "1":
            # Llama a función menu_libros de otro módulo
            gestion_libros.menu_libros()
            print("opt 1")

        elif opcion == "2":
            # Llama a función menu_usuarios de otro módulo
            gestion_usuarios.menu_usuarios()
            print("opt 2")

        elif opcion == "3":
            # Llama a función menu_prestamos de otro módulo
            gestion_prestamos.menu_prestamos()
            print("opt 3")

        elif opcion == "4":
            print("Gracias por utilizar nuestra app")
            break

        else:
            print("Opción no válida. Vuelve a intentarlo")


gestion_libros = GestionLibros()
gestion_usuarios = GestionUsuarios()
gestion_prestamos = GestionPrestamos(gestion_libros, gestion_usuarios)
menu_principal(gestion_libros, gestion_usuarios, gestion_prestamos)