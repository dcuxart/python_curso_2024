# Funciones de validación
# ISBN

def validarIsbnFormat(isbn):
     if len(isbn) == 13 and isbn.isdigit():
          return True
     return False

def validarIsbnUnique(isbn, libros):
    for libro in libros:
        if libro['isbn'] == isbn:
            return False
    return True

# DNI

def validarDniFormat(dni):

     dni_digitos = dni[:8]
     dni_letra = dni[-1]

     if len(dni) != 9:
          return False
     elif not dni_digitos.isdigit() or not dni_letra.isalpha():
          return False
     else:
          return True

def validarDniUnique(dni, usuarios):
    for usuario in usuarios:
        if usuario['dni'] == dni:
            return False
    return True
    
# PRÉSTAMO

def validarPrestamo(isbn, prestamos):
     for prestamo in prestamos:
          if prestamo['isbn'] == isbn:
               return False
     return True

def validarDevolucionUnique(isbn, prestamos):
    for prestamo in prestamos:
        if prestamo['isbn'] != isbn:
            return False
    return True
