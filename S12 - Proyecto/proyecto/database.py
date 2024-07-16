import mysql.connector
from mysql.connector import Error

# constructor
class Database():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "apirest"
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