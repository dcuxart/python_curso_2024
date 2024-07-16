import utils

class Libro:
    def __init__(self, isbn,titulo, autor, genero):      
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class GestionLibros:
    def menu_libros(self):
        while True:
            print("---Gestión de libros---")
            print("1: Añadir un libro: ")
            print("2: Eliminar un libro (por ISBN): ")
            print("3: Buscar libros: ")
            print("4: Mostrar todos los libros: ")
            print("5: Volver al menú principal: ")
        
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.anadir_libro()
            elif opcion == "2":
                self.borrar_libro()
            elif opcion == "3":
                self.mostrar_libro()
            elif opcion == "4":
                self.mostrar_libros()
            elif opcion == "5":
                print("Bye")
                break
            else:
                print("Opción no válida")


    def anadir_libro(self):
        isbn = input("Introduce el isbn del libro: ")
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        genero = input("Introduce el género del libro: ")
        # TODO: validar estos datos
        libro = Libro(isbn, titulo, autor, genero)
        utils.set_libro_mysql(libro)
        print("Libro insertado con éxito")

    def borrar_libro(self):
        isbn = input("Introduce el ISBN del libro: ")
        if utils.delete_libro_mysql(isbn):
            print(f"Libro con ISBN {isbn} borrado")
        else:
            print(f"Libro con ISBN {isbn} no registrado")
            
    def mostrar_libro(self):
        isbn = input("Introduce el dni del usuario: ")
        if utils.find_libro_mysql(isbn):
            print(utils.find_libro_mysql(isbn))
        else:
            print("No se ha encontrado el libro con ISBN " + isbn)
        
    def mostrar_libros(self):
        if utils.get_libros_mysql():
            print(utils.get_libros_mysql())
        else:
            print("No hay libros registrados")