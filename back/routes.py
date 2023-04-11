from back import app, conexion
import json
from flask import render_template



@app.route('/')
@app.route('/getproducts')
def home_page():

     with conexion.cursor() as cursor:
          # En este caso no necesitamos limpiar ningún dato
          cursor.execute("SELECT *,FORMAT(price, 'N2') as price FROM Productos;")

          # Con fetchall traemos todas las filas

          result = cursor.fetchall()

          row_list = []
          for row in result:
               row_dict = {column[0]: row[i] for i, column in enumerate(cursor.description)}
               row_list.append(row_dict)



     return json.dumps(row_list)
