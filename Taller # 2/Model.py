
#definicion de la clase
class Departamento():
#Constructor
    def __init__(self,cod,nombre):
        self.cod=cod
        self.nombre=nombre
        print("cod: {} / nombre : {}".format(self.cod, self.nombre))

class Producto():

    def __init__(self, descrip, precio):
        self.descrip=descrip
        self.precio=precio
        print("descrip: {} / precio: {}".format(self.descrip, self.precio))

class Descuento():

    def __init__(self, porc, duracion):
        self.porc=porc
        self.duracion=duracion
        print("porc: {} / duracion: {}".format(self.porc, self.duracion))