# import bcrypt

from http.server import BaseHTTPRequestHandler, HTTPServer

# METODO GET
# Nuestras rutas/recursos:
# "/": "Hola soy la pagina de inicio"
# "/contact": "Hola soy la pagina de formulario de contacto"
# "/*/ruta_no_existente": "Devolvemos un 404 (codigo de pag no encontrada)"
# listado de codigo:
# https://developer.mozilla.org/es/docs/Web/HTTP/Status

# METODO POST
# Recibiremos un dato (JSON) mediante POST y mediante la extension "Thunder Client" y lo imprimos en servidor. Despues le enviamos un Ok al cliente
import mysql.connector
from mysql.connector import Error 

class Database:
    def conexion(self):
        try:
            connex = mysql.connector.connect(
                user="root",
                password="",
                host="localhost",
            )
            if connex.is_connected():
                return connex
        except Error as e:
            print("Error en MySQL: " + str(e))
        finally:
            print("Conexión a MySQL correcta")
    
    def createTable(self, conexionDB):
        try:
            cursor = conexionDB.cursor()
            cursor.execute("drop database if exists test")
            cursor.execute("create database test")
            cursor.execute("use test")
            cursor.execute("create table datos(id int primary key auto_increment, mensaje varchar(255))")
            cursor.close()
        except Error as e:
            print("Error en MySQL: " + str(e))

    def insertData(self, conexionDB, data):
        try:
            cursor = conexionDB.cursor()
            query = "insert into datos values (default, %s)"
            cursor.execute(query, (data,))
            conexionDB.commit()
            cursor.close()
            conexionDB.close()
        except Error as e:
            print("Error en MySQL: " + str(e))

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hola soy la pagina de inicio")
            return
        if self.path == "/contact":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hola soy la pagina de form de contacto")
            return
        self.send_response(404)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.end_headers()
        self.wfile.write("Página no encontrada".encode("utf-8"))
        return
    
    def do_POST(self):
        import json         
        content_length = int(self.headers["Content-Length"]) # logitud del contenido
        post_data = self.rfile.read(content_length) # lee el contenido
        data = json.loads(post_data.decode("utf-8")) # convertimos el dato que nos viene en json a diccionario
        # print(data) # { "mensaje": "Hola mundo!" }

        # Encriptacion
        # data =data["mensaje"]

        # # Generating Salt
        # salt = bcrypt.gensalt()
        # # Hashing Password
        # hash_mensaje = bcrypt.hashpw(
        #     password=data,
        #     salt=salt
        # )

        # interactuar con la DB
        db = Database()
        conexionDB = db.conexion()
        db.createTable(conexionDB)
        db.insertData(conexionDB, data["mensaje"])
        # preparo la respuesta
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"El dato ha sido almacenado en la DB correctamente!")
        return

def run():
    print("Inciando servidor...")
    server_address = ("localhost", 3000)
    server = HTTPServer(server_address, Servidor)
    print("Servidor Localhost escuchando peticiones por el puerto 3000")
    server.serve_forever()

run()



