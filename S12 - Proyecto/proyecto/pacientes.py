import json

def get_pacientes(db):
    resultado = db.query("select * from pacientes")
    resultado_format = [
        {
            "id": dato[0],
            "dni": dato[1],
            "nombre": dato[2],
            "apellido": dato[3],
            "email": dato[4]
        }
        for dato in resultado
    ]
    return json.dumps(resultado_format).encode("utf-8")


def post_paciente(db, post_data):
    paciente = json.loads(post_data.decode("utf-8"))
    db.execute("insert into pacientes values (default, %s, %s, %s, %s)", (paciente["dni"], paciente["nombre"], paciente["apellido"], paciente["email"]))
    db.close()
    response = json.dumps({"mensaje": "Paciente introducido correctamente en MySQL"}).encode("utf-8")
    return response


def put_paciente(db, post_data):
    paciente = json.loads(post_data.decode("utf-8"))
    rows = db.execute("update pacientes set dni = %s, nombre = %s, apellido = %s, email = %s where id = %s", (paciente["dni"], paciente["nombre"], paciente["apellido"], paciente["email"], paciente["id"]))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Paciente actualizado correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Paciente no encontrado"}).encode("utf-8")
        status_code = 404
    return status_code, response


def delete_paciente(db, post_data):
    paciente = json.loads(post_data.decode("utf-8"))
    rows = db.execute("delete from pacientes where id = %s", (paciente["id"],))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Paciente eliminado correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Paciente no encontrado"}).encode("utf-8")
        status_code = 404
    return status_code, response