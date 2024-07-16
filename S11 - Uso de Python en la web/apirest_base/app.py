# importar módulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# import bcrypt

from database import Database
from utils import validar_email

class ApiRestBase(BaseHTTPRequestHandler):
    # método que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        db = Database() # instancia que incluye la conexión
        if self.path == "/datos":
            resultado = db.query("select * from datos")
            resultado_format = [
                {
                    "id": mensaje[0],
                    "mensaje": mensaje[1]
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))

        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data.decode("utf-8"))

            email = mensaje["email"]

            if not validar_email(email):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "email incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return

            db = Database()
            # llamaos al método execute con el formato de consulta que evita la inyección de SQL
            db.execute("insert into datos values (default, %s)", (mensaje["mensaje"],))
            db.close()
            self.set_headers(201) # envío un 201 (recurso creado exitosamente) al método cabeceras
            # devolvemos un mensaje en formato json al cliente
            response = json.dumps({"mensaje": "Dato almacenado correctamente en MySQL"}).encode("utf-8")
            self.wfile.write(response)

        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # Devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_PUT(self):
        if self.path == "/dato":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data.decode("utf-8"))

            # para encontrar la id del registro utilizamos la navegacion "mensaje["id"]"
            db = Database()
            rows = db.execute("update datos set dato = %s where id = %s", (mensaje["mensaje"], mensaje["id"]))
            db.close()

            if rows > 0:
                self.set_headers(200)
                response = json.dumps({"mensaje": "Dato actualizado correctamente en MySQL"}).encode("utf-8")
                self.wfile.write(response)

            else:
                self.set_headers(404) # envío un 404 al método de cabeceras
                # Devolvemos un mensaje en formato JSON al cliente
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))
        
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # Devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/datos":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data.decode("utf-8"))

            # para encontrar la id del registro utilizamos la navegacion "mensaje["id"]"
            db = Database()
            rows = db.execute("delete from datos where id = %s", (mensaje["id"],))
            db.close()

            if rows > 0:
                self.set_headers(200)
                response = json.dumps({"mensaje": "Dato actualizado correctamente en MySQL"}).encode("utf-8")
                self.wfile.write(response)
                # update datos set dato = %s where id = %s (sentencia sql))
            else:
                self.set_headers(404) # envío un 404 al método de cabeceras
                # Devolvemos un mensaje en formato JSON al cliente
                self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
        
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # Devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

def run(server_class = HTTPServer, handle_class = ApiRestBase, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print("ApiRest Localhost escuchando peticiones por el puerto 3000")
    httpd.serve_forever()

run()