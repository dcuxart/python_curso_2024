# Funciones de validacion
# ISBN

def validar_isbn_format(isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def validar_isbn_unique(isbn, libros):
    for libro in libros:
        if libro.isbn == isbn:
            return False
    return True

# DNI

def validar_dni_format(dni):

     dni_digitos = dni[:8]
     dni_letra = dni[-1]

     if len(dni) != 9:
          return False
     elif not dni_digitos.isdigit() or not dni_letra.isalpha():
          return False
     else:
          return True

def validar_dni_unique(dni, usuarios):
    for usuario in usuarios:
        if usuario.dni == dni:
            return False
    return True

# Prestamo

def validar_prestamo(isbn, prestamos):
     for prestamo in prestamos:
          if prestamo.isbn == isbn:
               return False
     return True

def validar_devolucion_unique(isbn, prestamos):
    for prestamo in prestamos:
        if prestamo.isbn != isbn:
            return False
    return True

# Exportar

def exportar_json(database_lista, nombre_fichero):
    import os

    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # abspath: devuelve la ruta absoluta del fichero actual
    # print(directorio_actual)

    # dirname: devuelve la ruta del directorio padre/madre
    ruta_carpeta_json = os.path.join(directorio_actual, 'json')

    # join: une la ruta absoluta cn /json
    if not os.path.exists(ruta_carpeta_json):
        os.makedirs(ruta_carpeta_json)

    # escribir en el fichero json
    ruta_fichero = os.path.join(ruta_carpeta_json, nombre_fichero)

    import json
    with open(ruta_fichero, 'w') as file:
        json.dump([libro.__dict__ for libro in database_lista], file, indent = 4)