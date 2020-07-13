from Modelo_view import Ciudadview
from Modelo_models import Ciudad


class ControllerCiudad:
    def __init__(self):
        self.ciudad = self.getdatos_ciudad() 
        self._vista_ciudad = Ciudadview(self._ciudad)
     

    def getdatos_ciudad(self): 
        ciudad = Ciudad('Ciudad 1')
        return ciudad

    def llamarVistaciudad(self):
        self._vista_ciudad.datos_ciudad()

############################################################################################################
from Modelo_view import Subestacionview
from Modelo_models import Subestacion



class ControllerSubestacion:
    def __init__(self):
        self._subestacion = self.getdatos_subestacion() 
        self._vista_subestacion = Subestacionview(self._subestacion)
       

    def getdatos_subestacion(self): 
        subestacion = Subestacion('Subestacion de 1')
        return subestacion

    def llamarVistaSubestacion(self): 
        self._vista_subestacion.datos_subestacion()


#################################################################################################################
from Modelo_view import Operadorview
from Modelo_models import Operador

class ControllerOperador:
     def __init__(self):
         self._operador = self.getdatos_operador() 
         self._vista_operador = Operadorview(self._operador)

    def llamarVistaOperador(self): 
        self._vista_operador.datos_operador()




###############################################################################################################









    
