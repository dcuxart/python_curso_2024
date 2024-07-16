import utils

class Libro:
    def __init__(self, isbn, titulo, autor, genero):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

# Clase que contiene la gestión de todas las acciones sobre la entidad Libro.
class GestionLibros:
    def __init__(self):
        self.librosDB = []

    # Métodos de gestión de libros:
    # 1 - Método de imprimir el menú de Libros.
    def menu_libros(self):
        while True:
            print("---Gestión de libros---")
            print("1: Añadir un libro: ")
            print("2: Eliminar un libro (por ISBN): ")
            print("3: Buscar libros: ")
            print("4: Mostrar todos los libros: ")
            print("5: Volver al menú principal: ")

            opcion = input("Elige una opción")
        
            if opcion == "1":
                isbn = input("Introduce el isbn del libro: ")
                titulo = input("Introduce el título del libro: ")
                autor = input("Introduce el autor del libro: ")
                genero = input("Introduce el género del libro: ")
                self.anadir_libro(isbn, titulo, autor, genero)

            elif opcion == "2":
                isbn = input("Introduce el ISBN del libro que quieres eliminar: ")
                self.eliminar_libro(isbn)

            elif opcion == "3":
                busqueda = input("Introduce el isbn, título o autor del libro que quieres buscar")
                resultados = self.buscar_libro(busqueda, busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    for resultado in resultados:
                        print(f"ISBN: {resultado.isbn}, Título: {resultado.titulo}, Autor: {resultado.autor}")
                else:
                    print("No se encontraron resultados")

            elif opcion == "4":
                self.mostrar_libros()

            elif opcion == "5":
                break

    def anadir_libro(self, isbn, titulo, autor, genero):
        if not utils.validar_isbn_format(isbn):
            print("ISBN con formato incorrecto")
            return

        if not utils.validar_isbn_unique(isbn, self.librosDB):
            print("ISBN ya existente")
            return
        
        libro = Libro(isbn, titulo, autor, genero)
        self.librosDB.append(libro)
        print(f"Libro añadido: {libro.__dict__}")

    def eliminar_libro(self, isbn):
        for libro in self.librosDB:
            if libro.isbn == isbn:
                self.librosDB.remove(libro)
                print(f"El libro con {isbn} ha sido eliminado")
                return
        print("Libro no encontrado")

    def buscar_libro(self, isbn = None, titulo = None, autor = None):
        resultados = []

        for libro in self.librosDB:
            if isbn and isbn.lower() == libro.isbn:
                resultados.append(libro)
            elif titulo and titulo.lower() == libro.titulo.lower():
                resultados.append(libro)
            elif autor and autor.lower() == libro.autor.lower():
                resultados.append(libro)

        return resultados

    def mostrar_libros(self):
        if self.librosDB:
            print("Libros disponibles: ")
            for libro in self.librosDB:
                print(f"ISBN: {libro.isbn}, Título: {libro.titulo}, Autor: {libro.autor}")
        else:
            print("No se encontraron libros disponibles")


# Instancias
# libro = Libro()

# libro1 = Libro('1111111111111', '1984', 'George Orwell', 'Distopico')
# libro1.__dict__
