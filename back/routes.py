
import random
import string
from back import app, conexion
import json
from datetime import datetime, timedelta




#FUNCIONES PRODUCTOS
@app.route('/getproducts')
def getproducts():

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


#FUNCIONES USUARIOS
@app.route('/login/<username>/<pwd>')
def login(username,pwd):

     with conexion.cursor() as cursor:

          cursor.execute("SELECT password FROM Usuarios WHERE user_ID=?;",(username,) )

          temppwd=cursor.fetchone()
          if temppwd:
               temppwd=temppwd[0]
               if temppwd==pwd:
                    print('TODO OK')
                    cookie = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
                    cursor.execute("SELECT token FROM Tokens WHERE token=?;", (cookie,))
                    tempcookie = cursor.fetchone()

                    while tempcookie:
                         cookie = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
                         cursor.execute("SELECT token FROM Tokens WHERE token=?;", (cookie,))
                         tempcookie = cursor.fetchone()

                    if not tempcookie:
                         hora_actual = datetime.now()
                         hora_proxima = hora_actual + timedelta(hours=1)
                         fecha_hora_actual = hora_actual.strftime('%Y-%m-%d %H:%M:%S')
                         fecha_hora_proxima = hora_proxima.strftime('%Y-%m-%d %H:%M:%S')
                         cursor.execute('INSERT INTO Tokens (user_ID,token,created_at, expires_at) VALUES (?, ?,?,?)',
                         username,cookie,fecha_hora_actual, fecha_hora_proxima)
                         print(cookie)
                         return cookie


               else:
                    print('PWD NOT MATCH')
          else:
               print('user not found')


     return
