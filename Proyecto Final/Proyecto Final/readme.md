# API REST (Servidor Web) base que nos sirve para desarrollar el proycto final de curso de Python.

# Estructura del proyecto
/apirest_base/
    |---------------/sql                -> Scripts SQL para la estructura de la DB
    |---------------/app.py             -> Punto de entrada de la apriest (toda la lógica del servidor web)
    |---------------/database.py        -> Clase con lógica de interacción a MySQL
    |---------------/doctores.py        -> Funciones con lógica de interacción a app.py
    |---------------/pacientes.py       -> Funciones con lógica de interacción a app.py
    |---------------/citas.py           -> Funciones con lógica de interacción a app.py
    |---------------/utils.py           -> Funciones con lógica de interacción a app.py
    |---------------/requirements.txt   -> Archivo que contiene todos los módulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los módulos de este archivo y los instale en nuestro proyecto.
```
pip install -r requirements.txt
```

# Crear entorno virtual y activarlo
```
python -m venv venv
```
```
venv\Scripts\activate

# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/doctores -> Devuelve todos los datos de la tabla "doctores" (cRud)
    - body: None

# GET: http://localhost:3000/pacientes -> Devuelve todos los datos de la tabla "pacientes" (cRud)
    - body: None

# GET: http://localhost:3000/citas -> Devuelve todos los datos de la tabla "citas" (cRud)
    - body: None

# POST: http://localhost:3000/doctor -> Crea/Inserta un dato (str) en la tabla "doctores" (Crud)
    - body (json): {"id": "dato_tipo_integer", "colegiado": "dato_tipo_texto", "nombre": "dato_tipo_texto", "especialidad": "dato_tipo_texto", "password": "dato_tipo_texto"}

# POST: http://localhost:3000/paciente -> Crea/Inserta un dato (str) en la tabla "pacientes" (Crud)
    - body (json): {"id": "dato_tipo_integer", "dni": "dato_tipo_texto", "nombre": "dato_tipo_texto", "apellido": "dato_tipo_texto", "email": "dato_tipo_texto"}

# POST: http://localhost:3000/cita -> Crea/Inserta un dato (str) en la tabla "citas" (Crud)
    - body (json): {"id": "dato_tipo_integer", "id_doctor": "dato_tipo_integer", "id_paciente": "dato_tipo_integer", "fecha_cita": "dato_tipo_date"} 

# PUT: http://localhost:3000/doctor -> Actualiza un dato (str) en la tabla "doctores" (crUd)
    - body (json): {id: "id_del_dato_a_actualizar", "colegiado": "dato_tipo_texto", "nombre": "dato_tipo_texto", "especialidad": "dato_tipo_texto", "password": "dato_tipo_texto"}

# PUT: http://localhost:3000/paciente -> Actualiza un dato (str) en la tabla "pacientes" (crUd)
    - body (json): {id: "id_del_dato_a_actualizar", "dni": "dato_tipo_texto", "nombre": "dato_tipo_texto", "apellido": "dato_tipo_texto", "email": "dato_tipo_texto"}

# PUT: http://localhost:3000/cita -> Actualiza un dato (str) en la tabla "citas" (crUd)
    - body (json): {id: "id_del_dato_a_actualizar", "id_doctor": "dato_tipo_integer", "id_paciente": "dato_tipo_integer", "fecha_cita": "dato_tipo_date"}

# DELETE: http://localhost:3000/doctor -> Borra un dato (str) en la tabla "doctores" (cruD)
    - body (json): {id: "id_del_dato_a_borrar",}

# DELETE: http://localhost:3000/paciente -> Borra un dato (str) en la tabla "pacientes" (cruD)
    - body (json): {id: "id_del_dato_a_borrar",}

# DELETE: http://localhost:3000/cita -> Borra un dato (str) en la tabla "citas" (cruD)
    - body (json): {id: "id_del_dato_a_borrar",}