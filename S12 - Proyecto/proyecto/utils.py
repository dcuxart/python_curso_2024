import re
import bcrypt


def validar_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.+-]+$"
    email_match = re.match(email_pattern, email)
    return(bool(email_match))


def validar_dni(dni):
    dni_pattern = r"^\d{8}[A-Z]$"
    dni_match = re.match(dni_pattern, dni)
    return bool(dni_match)


def encriptar_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def validar_fecha(fecha):
    fecha_pattern = r"^\d{4}-\d{2}-\d{2}$"
    date_match = re.match(fecha_pattern, fecha)
    return date_match