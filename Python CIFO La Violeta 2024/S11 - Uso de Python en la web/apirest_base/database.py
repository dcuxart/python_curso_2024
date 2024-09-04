import mysql.connector
from mysql.connector import Error


# constructor: Cada vez que se realiza una instancia a esta clase tenemos una conexión a MySQL en "self.connection."
class Database():
    def __init__(self):
        # Gestinamos si hay error en la conexión MySQL mediante excepciones
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "apirest_base"
            )
        except Error as e:
            print("Error en MySQL" + str(e))        

        self.cursor = self.connection.cursor()

# Método consulta
    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

# Método ejecución
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount

# Método cerrar
    def close(self):
        self.cursor.close()
        self.connection.close()