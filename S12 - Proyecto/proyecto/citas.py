import json

def get_citas(db):
    resultado = db.query("select * from citas")
    resultado_format = [
        {
            "id": dato[0],
            "id_doctor": dato[1],
            "id_paciente": dato[2],
            "fecha_cita": dato[3].strftime("%d/%m/%Y")
        }
        for dato in resultado
    ]
    return json.dumps(resultado_format).encode("utf-8")


def post_cita(db, post_data):
    cita = json.loads(post_data.decode("utf-8"))
    db.execute("insert into citas values (default, %s, %s, %s)", (cita["id_doctor"], cita["id_paciente"], cita["fecha_cita"]))
    db.close()
    response = json.dumps({"mensaje": "Cita introducida correctamente en MySQL"}).encode("utf-8")
    return response


def put_cita(db, post_data):
    cita = json.loads(post_data.decode("utf-8"))
    rows = db.execute("update citas set id_doctor = %s, id_paciente = %s, fecha_cita = %s where id = %s", (cita["id_doctor"], cita["id_paciente"], cita["fecha_cita"], cita["id"]))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Cita actualizada correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Cita no encontrada"}).encode("utf-8")
        status_code = 404
    return status_code, response


def delete_cita(db, post_data):
    cita = json.loads(post_data.decode("utf-8"))
    rows = db.execute("delete from citas where id = %s", (cita["id"],))
    db.close()
    if rows > 0:
        response = json.dumps({"mensaje": "Cita eliminada correctamente en MySQL"}).encode("utf-8")
        status_code = 200
    else:
        response = json.dumps({"error": "Cita no encontrada"}).encode("utf-8")
        status_code = 404
    return status_code, response