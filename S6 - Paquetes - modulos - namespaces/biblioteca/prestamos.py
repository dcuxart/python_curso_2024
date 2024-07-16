import libros
import usuarios
import utils

prestamos = []

def menuPrestamo():
    while True:
        print("---Gestión de Préstamos---")
        print("1: Registrar un préstamo")
        print("2: Devolver libro")
        print("3: Mostrar préstamos por usuario")
        print("4: Mostrar todos los préstamos")
        print("5: Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            isbn = input("Introduce el ISBN que quieres retirar: ")
        
            if not utils.validarIsbnFormat(isbn):
                print("ISBN con formato incorrecto")
                return
        
            if not utils.validarPrestamo(isbn, prestamos):
                print("Libro no disponible")
                return

            dni = input("Introduce el DNI de tu usuario")
        
            if not utils.validarDniFormat(dni):
                print("DNI con formato incorrecto")
                return

            registrarPrestamo(isbn, dni)

        if opcion == "2":
            isbn = input("Introduce el ISBN del libro que quieres devolver: ")

            if not utils.validarIsbnFormat(isbn):
                print("ISBN con formato incorrecto")
                return
            
            # if not utils.validarPrestamoUnique(isbn, prestamos):
            #     print("Libro con ISBN no está en préstamos")
            #     return
            
            devolverLibro(isbn)

        if opcion == "3":
            dni = input("Introduce el DNI del usuario para ver sus préstamos: ")

            mostrarPrestamosUsuario(dni)

        if opcion == "4":
            mostrarPrestamos()

        elif opcion == '5':
            break
    

def registrarPrestamo(isbn, dni):

    prestamo = {'isbn' : isbn, 'dni' : dni}

    prestamos.append(prestamo)
    print(prestamos)


def devolverLibro(isbn):
    for prestamo in prestamos:
        if prestamo['isbn'] == isbn:
            prestamos.remove(prestamo)
            print(f"Libro con {isbn} devuelto")
            print(prestamos)
            return
    print('Préstamo no encontrado')


def mostrarPrestamosUsuario(dni):
    for prestamo in prestamos:
        if prestamo['dni'] == dni:
            print(f"ISBN: {prestamo['isbn']}, Usuario: {prestamo['dni']}")
        else:
            print("No hay libros disponibles")


def mostrarPrestamos():
    if prestamos:
        print("Libros prestados: ")
        for prestamo in prestamos:
            print(f"ISBN: {prestamo['isbn']}, Título: {prestamo['dni']}")
    else:
        print("No hay libros prestados")