import json

def get_doctores(db):
    resultado = db.query("select * from doctores")
    resultado_format = [
        {
            "id": dato[0],
            "colegiado": dato[1],
            "nombre": dato[2],
            "especialidad": dato[3],
            "password": dato[4]
        }
        for dato in resultado
    ]
    return json.dumps(resultado_format).encode("utf-8")


def post_doctor(db, post_data, hash_password):
    doctor = json.loads(post_data.decode("utf-8"))
    db.execute("insert into doctores values (default, %s, %s, %s, %s)", (doctor["colegiado"], doctor["nombre"], doctor["especialidad"], hash_password))
    db.close()
    response = json.dumps({"mensaje": "Doctor introducido correctamente en MySQL"}).encode("utf-8")
    return response


def put_doctor(db, post_data):
    doctor = json.loads(post_data.decode("utf-8"))
    rows = db.execute("update doctores set colegiado = %s, nombre = %s, especialidad = %s, password = %s where id = %s", (doctor["colegiado"], doctor["nombre"], doctor["especialidad"], doctor["password"], doctor["id"]))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Doctor actualizado correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Doctor no encontrado"}).encode("utf-8")
        status_code = 404
    return status_code, response


def delete_doctor(db, post_data):
    doctor = json.loads(post_data.decode("utf-8"))
    rows = db.execute("delete from doctores where id = %s", (doctor["id"],))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Doctor eliminado correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Doctor no encontrado"}).encode("utf-8")
        status_code = 404
    return status_code, response