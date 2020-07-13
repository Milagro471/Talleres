import sqlite3 as base
from sqlite3 import Error

def stringconexion():
    try:
        conexion = base.connect("ICE.db")
        return conexion
    except Error as err:
        print(err)


########################################tabla Operador#####################################################
def Operador(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("Create table Operador(id integer primary key autoincrement not null, Nombre_operador text)")
        cursor.commit()
    except Error:
        print(Error, "Ingrese los datos solicitados")

def insertaroperador(connection, medidor):
    try:
        cursor = connection.cursor()
        cursor.execute("Insertar into Operador(id, Nombre_operador) values(?,?)", medidor)
        cursor.commit()
    except Error:
        print(Error, "Los datos se han ingresado")

def actualizaroperador(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("Update Operador set Nombre_operador=Allan where Nombre_operador= Milagro")
        cursor.commit()
    except Error:
        print(Error,"Los datos no se actualizaron correctamente!")


#########################################################inertar y actualizar datos######################################

base = stringconexion()
Operador(base)

# creo tupletas con los valores a inyectar en mi query de INSERT
medidor_1 = ("Juan")
medidor_2 = ("Maria")
medidor_3 = ("Milagro")
         

medidor_dict = {
        1: medidor_1,
        2: medidor_2,
        3: medidor_3
}

# Inyecto INSERT INTO table con valores pretederminados
for key in medidor_dict:
    print(medidor_dict[key])
    insertaroperador(base, medidor_dict[key])


def get_all_rows(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Operador") # SOLO EJECUTA
        objeto_resultado = cursor.fetchall() # TODOS LOS REGISTROS QUE DEVOLVIO EL QUERY
        connection.commit()

        return objeto_resultado

    except Error:
        print(Error, "Debieron ser valores erroneos!")

resultado = get_all_rows(base)

for item in resultado:
    print("REGISTRO: ", item)

actualizaroperador(base)

# 
resultado = get_all_rows(base)

for item in resultado:
    print("REGISTRO: ", item)
