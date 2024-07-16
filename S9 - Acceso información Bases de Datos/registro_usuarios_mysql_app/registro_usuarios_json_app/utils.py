# CONEXIÓN

def conexion_a_mysql():
    import mysql.connector

    connex = mysql.connector.connect(
        user = "root",
        password = "",
        host = "localhost",
        database = "app"
    )
    if connex.is_connected():
        return connex


# USUARIOS

def set_usuario_mysql(usuarioObj):
    connex = conexion_a_mysql()
    cursor_set = connex.cursor()

    query = "insert into usuarios values(null, %s, %s, %s, %s)" # Más seguridad/ Evitar inyección SQL - brecha seguridad
    cursor_set.execute(query, (usuarioObj.dni, usuarioObj.nombre, usuarioObj.email, usuarioObj.password))

    connex.commit()
    cursor_set.close()


def get_usuarios_mysql():
    connex = conexion_a_mysql()
    cursor_get = connex.cursor()

    query = "select * from usuarios"
    cursor_get.execute(query)

    usuarios = cursor_get.fetchall()
    cursor_get.close
    connex.close()
    return usuarios #Lo devuelve como una tupla

    # key = {None, 'dni', 'nombre', 'email', 'password'}

    # dic = [dict(zip(key, value)) for value in datos]
    # return dic


def delete_usuario_mysql(dni):

    if find_usuario_mysql(dni):
        connex = conexion_a_mysql()
        cursor_delete = connex.cursor()

        query = "delete from usuarios where dni = %s"
        cursor_delete.execute(query, (dni,))
        connex.commit()

        filas_afectadas = cursor_delete.rowcount
        cursor_delete.close()
        connex.close()

        if filas_afectadas > 0:
            return True
        else:
            return False


def find_usuario_mysql(dni):
    connex = conexion_a_mysql()
    cursor_find = connex.cursor()

    query = "select * from usuarios where dni = %s"
    cursor_find.execute(query, (dni,))

    usuario = cursor_find.fetchall()
    cursor_find.close()
    connex.close()
    return usuario

# LIBROS

def set_libro_mysql(libroObj):
    connex = conexion_a_mysql()
    cursor_set = connex.cursor()

    query = "insert into libros values(null, %s, %s, %s, %s)"
    cursor_set.execute(query, (libroObj.isbn, libroObj.titulo, libroObj.autor, libroObj.genero))

    connex.commit()
    cursor_set.close()


def get_libros_mysql():
    connex = conexion_a_mysql()
    cursor_get = connex.cursor()

    query = "select * from libros"
    cursor_get.execute(query)

    libros = cursor_get.fetchall()
    cursor_get.close
    connex.close()
    return libros


def delete_libro_mysql(isbn):

    if find_libro_mysql(isbn):
        connex = conexion_a_mysql()
        cursor_delete = connex.cursor()

        query = "delete from libros where isbn = %s"
        cursor_delete.execute(query, (isbn,))
        connex.commit()

        filas_afectadas = cursor_delete.rowcount
        cursor_delete.close()
        connex.close()

        if filas_afectadas > 0:
            return True
        else:
            return False


def find_libro_mysql(isbn):
    connex = conexion_a_mysql()
    cursor_find = connex.cursor()

    query = "select * from libros where isbn = %s"
    cursor_find.execute(query, (isbn,))

    libro = cursor_find.fetchall()
    cursor_find.close()
    connex.close()
    return libro

# PRÉSTAMOS

def set_prestamo_mysql(prestamoObj):
    connex = conexion_a_mysql()
    cursor_set = connex.cursor()

    query = "insert into prestamos values(null, %s, %s, %s)"
    cursor_set.execute(query, (prestamoObj.isbn, prestamoObj.dni, prestamoObj.fecha))

    connex.commit()
    cursor_set.close()


def get_prestamos_mysql():
    connex = conexion_a_mysql()
    cursor_get = connex.cursor()

    query = "select * from prestamos"
    cursor_get.execute(query)

    prestamos = cursor_get.fetchall()
    cursor_get.close
    connex.close()
    return prestamos


def delete_prestamo_mysql(isbn):

    if find_prestamo_mysql(isbn):
        connex = conexion_a_mysql()
        cursor_delete = connex.cursor()

        query = "delete from prestamos where isbn = %s"
        cursor_delete.execute(query, (isbn,))
        connex.commit()

        filas_afectadas = cursor_delete.rowcount
        cursor_delete.close()
        connex.close()

        if filas_afectadas > 0:
            return True
        else:
            return False
        

def find_prestamo_mysql(isbn):
    connex = conexion_a_mysql()
    cursor_find = connex.cursor()

    query = "select * from prestamos where isbn = %s"
    cursor_find.execute(query, (isbn,))

    prestamo = cursor_find.fetchall()
    cursor_find.close()
    connex.close()
    return prestamo

# DATOS

def set_data_mysql(userObj, tabla):
 connex = conexion_a_mysql()
 cursor = connex.cursor()

 if tabla == "usuarios":
    query = f"insert into {tabla} values(null, %s, %s, %s, %s, %s)"
    cursor.execute(query, (userObj.dni, userObj.nombre, userObj.email, userObj.password))
    connex.commit()
    cursor.close()
    connex.close()

 elif tabla == "libros":
    query = f"insert into {tabla} values(null, %s, %s, %s, %s)"
    cursor.execute(query, (userObj.isbn, userObj.titulo, userObj.autor, userObj.genero))
    connex.commit()
    cursor.close()
    connex.close()