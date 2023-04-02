from flask import Flask

app = Flask(__name__)

import pyodbc

direccion_servidor = 'localhost'
nombre_bd = 'test'
nombre_usuario = 'sa'
password = 'Contrasena1'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT *,FORMAT(price, 'N2') as price FROM Productos;")

        # Con fetchall traemos todas las filas
        products = cursor.fetchall()


except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()

from back import routes