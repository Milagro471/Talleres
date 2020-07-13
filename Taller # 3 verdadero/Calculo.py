#Taller # 3
#Estudiante: Milagro Muñoz Moya

#datos de entrada

import math


def calculo(Total_consumo, Horas, Ciudad):

    kwh = Total_consumo*Horas

    resultado = 'Ciudad ' + str(Ciudad) + '. Total de consumo ' + str(kwh) + ' KW' + '. Hora pico: ' + str(Horas)
    
    return resultado

hayMasDatos = 1

while hayMasDatos == 1:
    print("Medidor del ICE")

    print("Bienvenido Operador: favor registrese")
    
    Operador=str(input("Digite el nombre del Operador:  ")) 

    print(Operador)

    #menu de las subestaciones
    print("1-Subestacion del Norte")

    print("2-Subestacion del Sur")

    print("3-Subestacion del Este")
        
    Subestacion=int(input("Digite la Subestacion a la que pertenece: "))

    if Subestacion == 1:

        print("La Subestacion del Norte")

    else:
        if (Subestacion == 2):

            print("La Subestacion del Sur")

        else:

            if(Subestacion == 3):

                print("La Subestacion del Este")

            else:

                print("La opcion ingresada no es valida")
    ###############################################################################################################
    # menu de las ciudades
    print("1-Ciudad 1")

    print("2-Ciudad 2")

    print("3-Ciudad 3")
        
    Ciudad=int(input("Digite la Ciudad a la que pertenece: "))

    if Ciudad == 1:

        print("Ciudad 1")

    else:
        if (Ciudad == 2):

            print("Ciudad 2")

        else:

            if(Ciudad == 3):

                print("Ciudad 3")

            else:

                print("La opcion ingresada no es valida")

    ############################################################################################################

    Total_consumo=float(input("Digite el total  del consumo realizado: "))

    ###########################################################################################################

    Horas=int(input("Digite las horas pico:  "))

    ############################################################################################################
    # metodo para realizar el calculo

    print('Reporte de operador: ' + Operador)

    resultado = calculo(Total_consumo, Horas, Ciudad)
    print(resultado)

    hayMasDatos = int(input("¿Quiere seguir? <Si(1)-No(2)>: "))








    




