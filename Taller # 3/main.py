from Modelo_controller import ControllerCiudad
from Modelo_controller import ControllerSubestacion
from Modelo_controller import ControllerOperador


if __name__=='__main__':

    print("Medidor del ICE")

    print("Bienvenido Operador: favor registrese")
 
    Operador=str(input("Digite el nombre del Operador:  ")) 

    print("Operador")
    ciudad =ControllerCiudad
    ciudad.llamarVistaciudad()



    subestacion= ControllerSubestacion
    subestacion.llamarVistaSubestacion()

    operadr= ControllerOperador
    operador.llamarVistaOperador()
    print("End.")
