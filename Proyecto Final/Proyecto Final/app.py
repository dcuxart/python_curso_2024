from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from database import Database
from doctores import get_doctores, post_doctor, put_doctor, delete_doctor
from pacientes import get_pacientes, post_paciente, put_paciente, delete_paciente
from citas import get_citas, post_cita, put_cita, delete_cita
from utils import validar_email, validar_dni, encriptar_password, validar_fecha


class ApiRest(BaseHTTPRequestHandler):
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        db = Database()
        if self.path == "/doctores":
            resultado_format = get_doctores(db)
            self.set_headers()
            self.wfile.write(resultado_format)

        elif self.path == "/pacientes":
            resultado_format = get_pacientes(db)
            self.set_headers()
            self.wfile.write(resultado_format)

        elif self.path == "/citas":
            resultado_format = get_citas(db)
            self.set_headers()
            self.wfile.write(resultado_format)

        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


    def do_POST(self):
        if self.path == "/doctor":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            doctor = json.loads(post_data.decode("utf-8"))
            
            hash_password = encriptar_password(doctor["password"].encode("utf-8"))

            db = Database()
            response = post_doctor(db, post_data, hash_password)
            self.set_headers(201)
            self.wfile.write(response)

        elif self.path == "/paciente":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            paciente = json.loads(post_data.decode("utf-8"))

            email = paciente["email"]

            if not validar_email(email):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "email incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return
            
            dni = paciente["dni"]

            if not validar_dni(dni):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "dni incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return

            db = Database()
            response = post_paciente(db, post_data)
            self.set_headers(201)
            self.wfile.write(response)

        elif self.path == "/cita":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            cita = json.loads(post_data.decode("utf-8"))

            fecha = cita["fecha_cita"]

            if not validar_fecha(fecha):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "fecha con formato incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return

            db = Database()
            response = post_cita(db, post_data)
            self.set_headers(201)
            self.wfile.write(response)

        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_PUT(self):
        if self.path == "/doctor":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            db = Database()
            status_code, response = put_doctor(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        elif self.path == "/paciente":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            paciente = json.loads(post_data.decode("utf-8"))

            email = paciente["email"]

            if not validar_email(email):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "email incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return
            
            dni = paciente["dni"]

            if not validar_dni(dni):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "dni incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return

            db = Database()
            status_code, response = put_paciente(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        elif self.path == "/cita":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            cita = json.loads(post_data.decode("utf-8"))

            fecha = cita["fecha_cita"]

            if not validar_fecha(fecha):
                self.set_headers(400) # bad request
                response = json.dumps({"error": "fecha con formato incorrecto"}).encode("utf-8")
                self.wfile.write(response)
                return

            db = Database()
            status_code, response = put_cita(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/doctor":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            db = Database()
            status_code, response = delete_doctor(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        elif self.path == "/paciente":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            db = Database()
            status_code, response = delete_paciente(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        elif self.path == "/cita":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            db = Database()
            status_code, response = delete_cita(db, post_data)
            self.set_headers(status_code)
            self.wfile.write(response)

        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


def run(server_class = HTTPServer, handle_class = ApiRest, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print("ApiRest Localhost escuchando peticiones por el puerto 3000")
    httpd.serve_forever()

run()