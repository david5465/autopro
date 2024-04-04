import mysql.connector

class Cconexion:
    def ConexionBaseDeDatos():
        try:
            conexion=mysql.connector.connect(user='root',password='N2H2vWw7E', host='127.0.0.1', database='bd',port='3306')
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as error:
            print ("Error al conectar {}".format(error))
            print("Conexión incorrecta")
            return conexion
    ConexionBaseDeDatos()       