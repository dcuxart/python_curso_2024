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