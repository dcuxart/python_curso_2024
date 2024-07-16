# API REST (Servidor Web) base que nos sirve para desarrollar el proycto final de curso de Python.

# Estructura del proyecto
/apirest_base/
    |---------------/sql                -> Scripts SQL para la estructura de la DB
    |---------------/app.py             -> Punto de entrada de la apriest (toda la lógica del servidor web)
    |---------------/database.py        -> Clase con lógica de interacción a MySQL
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
# GET: http://localhost:3000/datos -> Devuelve todos los datos de la tabla "datos" (cRud)
    - body: None

# POST: http://localhost:3000/dato -> Crea/Inserta un dato (str) en la tabla "datos" (Crud)
    - body (json): {"mensaje": "dato_tipo_texto"} 

# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "datos" (crUd)
    - body (json): {id: "id_del_dato_a_actualizar", "mensaje": "dato_tipo_texto"}

# DELETE: http://localhost:3000/dato -> Borra un dato (str) en la tabla "datos" (cruD)
    - body (json): {id: "id_del_dato_a_borrar"}



# Pasos desarrollo
1 - Crear el archivo "database.sql" que contiene la estructura de la base de datos en MySQL (DB relacional).
Esta base de datos contiene solamente una tabla con un campo "dato" en el que interactua la api rest.

2 - Coonstructor: Crea la conexión a MySQL
    - Constructor: Crea la conexión a MySQL
    - 3 métodos que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3 - Desarrollar la API REST en "/app/.py"
    1 - Añadir los imports que necesita este módulo.
    2 - Desarrollamos la clase "ApiRestBase"

     (información que viaja junto al paquete (request, response))