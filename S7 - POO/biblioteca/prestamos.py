import utils

class Prestamo:
    def __init__(self, isbn, dni, fecha):
        self.isbn = isbn
        self.dni = dni
        self.fecha = fecha


class GestionPrestamos:
    def __init__(self, gestionLibros, gestionUsuarios):
        self.prestamosDB = []
        self.gestionLibros = gestionLibros
        self.gestionUsuarios = gestionUsuarios

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

                dni = input("Introduce el DNI de tu usuario").upper()
            
                if not utils.validar_dni_format(dni):
                    print("DNI con formato incorrecto")
                    return
                
                fecha = input("Introduce la fecha del préstamo")
                
                self.registrar_prestamo(isbn, dni, fecha)

            if opcion == "2":
                busqueda = input("Introduce el ISBN del libro que quieres devolver: ")

                if not utils.validar_isbn_format(isbn):
                    print("ISBN con formato incorrecto")
                    return

                self.devolver_libro(busqueda)

            if opcion == "3":
                busqueda = input("Introduce el DNI o ISBN del préstamo que quieres buscar: ")
                resultados = self.buscar_prestamo(busqueda, busqueda)

                if resultados:
                    print("Resultados de la búsqueda: ")
                    for prestamo in resultados:
                        print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
                else:
                    print("No se encontraron resultados")

            if opcion == "4":
                self.mostrar_prestamos()

            elif opcion == '5':
                break


    def registrar_prestamo(self, isbn, dni, fecha):

        resultados = self.gestionUsuarios.buscar_usuario(dni)
        if not resultados:
            print(f"No se ha encontrado el usuario con {dni}")

        #TODO validar libro

        prestamo = Prestamo(isbn, dni, fecha)
        self.prestamosDB.append(prestamo)
        print(f"Préstamo registrado: {prestamo.__dict__}")


    def devolver_libro(self, isbn):
        for prestamo in self.prestamosDB:
            if prestamo.isbn == isbn:
                self.prestamosDB.remove(prestamo)
                print(f"Libro con {isbn} devuelto")
                print(prestamo.__dict__)
                return
        print('Préstamo no encontrado')


    def buscar_prestamo(self, isbn = None, dni = None):
        resultados = []

        for prestamo in self.prestamosDB:
            if isbn and isbn.lower() == prestamo.isbn:
                resultados.append(prestamo)
            elif dni and dni.upper() == prestamo.dni:
                resultados.append(prestamo)
        return resultados


    def mostrar_prestamos(self):
        if self.prestamosDB:
            print("Libros prestados: ")
            for prestamo in self.prestamosDB:
                print(f"ISBN: {prestamo.isbn}, DNI: {prestamo.dni}")
        else:
            print("No hay libros prestados")