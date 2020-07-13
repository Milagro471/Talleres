
class Ciudadview:

    def _init_(self,ciudad):

        self.datos_ciudad = ciudad

    def datos_ciudad(self):

        print("view Ciudad:  " + repr(self.datos_ciudad))
    

class Subestacionview:

    def __init__(self, subestacion):

        self.datos_subestacion = subestacion

    def datos_subestacion(self):

        print("view Subestacion: " + repr(self.datos_subestacionsubestacion))

class Operadorview:

    def __init__(self, operador):

        self. datos_operador = operador

    def datos_operador(self):

        print("View Operador: " + repr(self.datos_operador))
