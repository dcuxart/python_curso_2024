import utils

class Prestamos:
    def __init__(self, isbn, dni, fecha):
        self.isbn = isbn
        self.dni = dni
        self.fecha = fecha


class GestionPrestamos:
    def __init__(self, gestionLibros, gestionUsuarios):
        self.prestamosDB = []

    def menuPrestamos(self):
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
            
                if not utils.validar_isbn_format(isbn):
                    print("ISBN con formato incorrecto")
                    return
            
                if not utils.validar_prestamo(isbn, self.prestamosDB):
                    print("Libro no disponible")
                    return

                dni = input("Introduce el DNI de tu usuario")
            
                if not utils.validar_dni_format(dni):
                    print("DNI con formato incorrecto")
                    return
                
                self.registrar_prestamo(isbn, dni)

            if opcion == "2":
                isbn = input("Introduce el ISBN del libro que quieres devolver: ")

                if not utils.validar_isbn_format(isbn):
                    print("ISBN con formato incorrecto")
                    return

                self.devolver_libro(isbn)

            if opcion == "3":
                dni = input("Introduce el DNI del usuario para ver sus préstamos: ")

            self.mostrar_prestamos_usuario(dni)

            if opcion == "4":
                self.mostrar_prestamos()

            elif opcion == '5':
                break


    def registrar_prestamo(self, isbn, dni, fecha):

        resultados = self.gestionUsuarios.buscar_usuario(dni)
        if not resultados:
            print(f"No se ha encontrado el usuario con {dni}")

        #TODO validar libro

        prestamo = Prestamos(isbn, dni, fecha)
        self.prestamosDB.append(prestamo)
        print(prestamo.__dict__)


    def devolver_libro(self, isbn):
        for prestamo in self.prestamosDB:
            if prestamo.isbn == isbn:
                self.prestamosDB.remove(prestamo)
                print(f"Libro con {isbn} devuelto")
                print(prestamo.__dict__)
                return
        print('Préstamo no encontrado')


    def mostrar_prestamos_usuario(self, dni):
        for prestamo in self.prestamosDB:
            if prestamo.dni == dni:
                print(f"ISBN: {prestamo.isbn}, Usuario: {prestamo.dni}")
            else:
                print("No hay libros disponibles")


    def mostrar_prestamos(self):
        if self.prestamosDB:
            print("Libros prestados: ")
            for prestamo in self.prestamosDB:
                print(f"ISBN: {prestamo.isbn}, Título: {prestamo.dni}")
        else:
            print("No hay libros prestados")