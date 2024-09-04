import utils

usuarios = []

def menuUsuario():
    while True:
        print("---Gestión de usuarios---")
        print("1: Añadir un usuario: ")
        print("2: Eliminar un usuario (por dni): ")
        print("3: Buscar usuarios: ")
        print("4: Mostrar todos los usuarios: ")
        print("5: Volver al menú principal: ")

        opcion = input("Elige una opción")

        if opcion == "1":
            dni = input("Introduce el DNI del usuario: ").upper()

            if not utils.validarDniFormat(dni):
                print("DNI con formato incorrecto")
                return
            if not utils.validarDniUnique(dni, usuarios):
                print("DNI ya existente")
                return
            
            nombre = input("Introduce el nombre del usuario: ")
            apellido = input("Introduce el apellido del usuario: ")
            correo = input("Introduce el correo del usuario: ")

            anadirUsuario(dni, nombre, apellido, correo)

        if opcion == "2":
            dni = input("Introduce el dni")
            eliminarUsuario(dni)

        if opcion == "3":
            busqueda = input("Introduce el dni o el correo del usuario que quieres buscar")
            resultados = buscarUsuario(busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"DNI: {resultado['dni']}, Nombre: {resultado['nombre']}, Apellido: {resultado['apellido']}, Correo: {resultado['correo']}")
            else:
                print("No se encontraron resultados")            

        if opcion == "4":
            mostrarUsuarios()
            
        elif opcion == '5':
            break

def anadirUsuario(dni, nombre, apellido, correo):

    # if not utils.validarDniFormat(dni_param):
    #     print("DNI con formato incorrecto")
    #     return

    # if not utils.validarDniUnique(dni_param, usuarios):
    #     print("DNI ya existente")
    #     return

    usuario = {'dni' : dni, 'nombre' : nombre, 'apellido' : apellido, 'correo' : correo}

    usuarios.append(usuario)
    print(usuarios)

def eliminarUsuario(dni):
    for usuario in usuarios:
        if usuario['dni'] == dni:
            usuarios.remove(usuario)
            print(f"Usuario con {dni} eliminado")
            print(usuarios)
            return
    print('Usuario no encontrado')

def mostrarUsuarios():
    if usuarios:
        print("Usuarios registrados: ")
        for usuario in usuarios:
            print(f"DNI: {usuario['dni']}, Nombre: {usuario['nombre']}, Apellido: {usuario['apellido']}, Correo: {usuario['correo']}")
    else:
        print("No hay usuarios")

def buscarUsuario(dni = None, correo = None):
    resultados = []

    for usuario in usuarios:
        if dni and dni.lower() == usuario['dni'].lower():
            resultados.append(usuario)
        elif correo and correo.lower() == usuario['correo'].lower():
            resultados.append(usuario)

    return resultados