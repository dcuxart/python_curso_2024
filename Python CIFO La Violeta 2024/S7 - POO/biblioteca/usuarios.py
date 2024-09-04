import utils

usuarios = []

class Usuario:
    def __init__(self, dni, nombre, apellido, correo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


class GestionUsuarios:
    def __init__(self):
        self.usuariosDB = []

    def menu_usuarios(self):
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

                if not utils.validar_dni_format(dni):
                    print("DNI con formato incorrecto")
                    return
                
                if not utils.validar_dni_unique(dni, usuarios):
                    print("DNI ya existente")
                    return
                
                nombre = input("Introduce el nombre del usuario: ")
                apellido = input("Introduce el apellido del usuario: ")
                correo = input("Introduce el correo del usuario: ").lower()

                self.anadir_usuario(dni, nombre, apellido, correo)

            if opcion == "2":
                dni = input("Introduce el dni")
                self.eliminar_usuario(dni)

            if opcion == "3":
                busqueda = input("Introduce el dni o el correo del usuario que quieres buscar")
                resultados = self.buscar_usuario(busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    for resultado in resultados:
                        print(f"DNI: {resultado.dni}, Nombre: {resultado.nombre}, Apellido: {resultado.apellido}, Correo: {resultado.correo}")
                else:
                    print("No se encontraron resultados")            

            if opcion == "4":
                self.mostrar_usuarios()
                
            elif opcion == '5':
                break

    def anadir_usuario(self, dni, nombre, apellido, correo):

        usuario = Usuario(dni, nombre, apellido, correo)
        self.usuariosDB.append(usuario)
        print(f"Usuario añadido: {usuario.__dict__}")

    def eliminar_usuario(self, dni):
        for usuario in self.usuariosDB:
            if usuario.dni == dni:
                self.usuariosDB.remove(usuario)
                print(f"Usuario con {dni} eliminado")
                return
        print('Usuario no encontrado')

    def mostrar_usuarios(self):
        if self.usuariosDB:
            print("Usuarios registrados: ")
            for usuario in self.usuariosDB:
                print(f"DNI: {usuario.dni}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Correo: {usuario.correo}")
        else:
            print("No hay usuarios rgistrados")

    def buscar_usuario(self, dni = None, correo = None):
        resultados = []

        for usuario in self.usuariosDB:
            if dni and dni.lower() == usuario.dni.lower():
                resultados.append(usuario)
            elif correo and correo.lower() == usuario.correo.lower():
                resultados.append(usuario)

        return resultados