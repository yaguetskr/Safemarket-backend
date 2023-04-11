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




except Exception as e:
    print("Ocurrió un error al consultar: ", e)


from back import routes