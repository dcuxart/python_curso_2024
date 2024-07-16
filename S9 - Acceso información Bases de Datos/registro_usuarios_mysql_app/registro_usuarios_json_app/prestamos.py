import utils

class Prestamo:
    def __init__(self, isbn, dni, fecha):
        self.isbn = isbn
        self.dni = dni
        self.fecha = fecha

class GestionPrestamos:
    def __init__(self, gestion_libros, gestion_usuarios):
        self.prestamosDB = []
        self.gestion_libros = gestion_libros
        self.gestion_usuarios = gestion_usuarios

    def menu_prestamos(self):
        while True:
            print("---Gestión de Préstamos---")
            print("1: Registrar un préstamo")
            print("2: Devolver libro")
            print("3: Mostrar préstamos por usuario")
            print("4: Mostrar todos los préstamos")
            print("5: Volver al menú principal")
        
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.anadir_prestamo()
            elif opcion == "2":
                self.borrar_prestamo()
            elif opcion == "3":
                self.mostrar_prestamo()
            elif opcion == "4":
                self.mostrar_prestamos()
            elif opcion == "5":
                print("Bye")
                break
            else:
                print("Opción no válida")


    def anadir_prestamo(self):
        isbn = input("Introduce el ISBN del libro: ")
        dni = input("Introduce tu dni: ")
        fecha = input("Introduce la fecha: ")
        # TODO: validar estos datos
        prestamo = Prestamo(isbn, dni, fecha)
        utils.set_prestamo_mysql(prestamo)
        print("Préstamo realizado con éxito")

    def borrar_prestamo(self):
        isbn = input("Introduce el ISBN del libro que quieres devolver: ")
        if utils.delete_prestamo_mysql(isbn):
            print(f"Libro con ISBN {isbn} devuelto")
        else:
            print(f"Libro con ISBN {isbn} no registrado")
            
    # def mostrar_prestamo(self):
    #     dni = input("Introduce el DNI del usuario o ISBN del libro que quieres buscar: ")

    #     dni = input("Introduce el dni del usuario: ")
    #     if utils.find_usuario_mysql(dni):
    #         print(utils.find_usuario_mysql(dni))
    #     else:
    #         print("No se ha encontrado el usuario con dni " + dni)
        
    # def mostrar_prestamos(self):
    #     if utils.get_prestamos_mysql():
    #         print(utils.get_prestamos_mysql())
    #     else:
    #         print("No hay préstamos registrados")