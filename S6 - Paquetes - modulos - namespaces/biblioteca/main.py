import libros
import usuarios
import prestamos

def menuPrincipal():
    while True:
        print("---Gestión de una biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción")

        if opcion == "1":
            # Llama a función menu_libros de otro módulo
            libros.menuLibros()
            print("opt 1")
        elif opcion == "2":
            # Llama a función menu_usuarios de otro módulo
            usuarios.menuUsuario()
            print("opt 2")
        elif opcion == "3":
            # Llama a función menu_prestamos de otro módulo
            prestamos.menuPrestamo()
            print("opt 3")
        elif opcion == "4":
            print("Gracias por utilizar nuestra app")
            break
        else:
            print("Opción no válida. Vuelve a intentarlo")

menuPrincipal()