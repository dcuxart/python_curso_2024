import utils

libros = []

def menuLibros():
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

            if not utils.validarIsbnFormat(isbn):
                print("ISBN con formato incorrecto")
                return
            if not utils.validarIsbnUnique(isbn, libros):
                print("ISBN ya existente")
                return    
            
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            genero = input("Introduce el género del libro: ")
            anadirLibro(isbn, titulo, autor, genero)

        if opcion == "2":
            isbn_param = input("Introduce el isbn")
            eliminarLibro(isbn_param)

        if opcion == "3":
            busqueda = input("Introduce el título, autor o ISBN que quieres buscar")
            resultados = buscarLibro(busqueda, busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"ISBN: {resultado['isbn']}, Título: {resultado['titulo']}, Autor: {resultado['autor']}, Género: {resultado['genero']}")
            else:
                print("No se encontraron resultados")
                
        if opcion == "4":
            mostrarLibro()

        elif opcion == "5":
            break

def anadirLibro(isbn, titulo, autor, genero):

    # if not utils.validarIsbnFormat(isbn):
    #     print("ISBN con formato incorrecto")
    #     return
    
    # if not utils.validarIsbnUnique(isbn, libros):
    #     print("ISBN ya existente")
    #     return
    
    libro = {'isbn' : isbn, 'titulo' : titulo, 'autor' : autor, 'genero' : genero}

    libros.append(libro)
    print(libros)

def eliminarLibro(isbn_param):
    for libro in libros:
        if libro['isbn'] == isbn_param:
            libros.remove(libro)
            print(f"Libro con {isbn_param} eliminado")
            print(libros)
            return
    print('Libro no encontrado')

def mostrarLibro():
    if libros:
        print("Libros disponibles: ")
        for libro in libros:
            print(f"ISB: {libro['isbn']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        print("No hay libros disponibles")

def buscarLibro(titulo = None, autor = None, isbn = None):
    resultados = []

    for libro in libros:
        if titulo and titulo.lower() == libro['titulo'].lower():
            resultados.append(libro)
        elif autor and autor.lower() == libro['autor'].lower():
            resultados.append(libro)
        elif isbn == libro['isbn']:
            resultados.append(libro)

    return resultados

