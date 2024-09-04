import re

def validar_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.+-]+$"
    email_match = re.match(email_pattern, email)
    return(bool(email_match))

# dni
def validar_dni(dni):
    dni_pattern = r"^\d{8}[A-Z]$"
    dni_match = re.match(dni_pattern, dni)
    return bool(dni_match)