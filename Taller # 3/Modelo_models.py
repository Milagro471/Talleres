class Ciudad:
    
    def __init__(self, codigo, horas): # se envia el objeto Instrumento como parametro
        self._codigo  = codigo
        self._horas = horas
        

    def __repr__(self):

        return ("Ciudad: {} | codigo: {}  horas {}".format(self._codigo, self._horas))


####################################################################################################################################

class Subestacion:
    def __init__(self, ciudad, total, hora_pico):
        self._ciudad = ciudad
        self._total = total
        self._hora_pico = hora_pico

    def __repr__(self): # representacion de un obj Instrumento

        return("Subestacion: {} | ciudad: {} | total: {} | hora_pico: {}".format(self._ciudad, self._total, self._hora_pico))


####################################################################################################################################


class Operador:
    def __init__(self, id, nombre):
        self._id=id
        self._nombre = nombre
    
    def __repr__ (self):

        return "El nombre del Operador es: "+ self._nombre


####################################################################################################################################
