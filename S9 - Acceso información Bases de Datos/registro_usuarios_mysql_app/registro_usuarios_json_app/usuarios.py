import utils

class Usuario:
    def __init__(self, dni, nombre, email, password):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.password = password

class GestionUsuarios:
    def menu_usuarios(self):
        while True:
            print("--Gestión Usuarios--")
            print("1: Añadir Usuario")
            print("2: Eliminar Usuario (dni)")
            print("3: Buscar Usuario (dni)")
            print("4: Mostrar todos los Usuarios")
            print("5: Salir")
        
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.anadir_usuario()
            elif opcion == "2":
                self.borrar_usuario()
            elif opcion == "3":
                self.mostrar_usuario()
            elif opcion == "4":
                self.mostrar_usuarios()
            elif opcion == "5":
                print("Bye")
                break
            else:
                print("Opción no válida")


    def anadir_usuario(self):
        dni = input("Introduce tu dni: ")
        nombre = input("Introduce tu nombre: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        # TODO: validar estos datos
        usuario = Usuario(dni, nombre, email, password)
        utils.set_data_mysql(usuario, "tabla")
        print("Usuario insertado con éxito")

    def borrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.delete_usuario_mysql(dni):
            print(f"Usuario con dni {dni} borrado")
        else:
            print(f"Usuario con dni {dni} no registrado")
            
    def mostrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.find_usuario_mysql(dni):
            print(utils.find_usuario_mysql(dni))
        else:
            print("No se ha encontrado el usuario con dni " + dni)
        
    def mostrar_usuarios(self):
        if utils.get_usuarios_mysql():
            print(utils.get_usuarios_mysql())
        else:
            print("No hay usuarios registrados")