
#Taller # 1
#Estudiante: Milagro Muñoz Moya

import math

Cantidad=int(input("Digite la cantidad de muestras :")) 

#ingresa al ciclo con el objetivo de que repita la cantidad de muestras ingresadas
for cont  in range(Cantidad):
    cont= cont + 1
    print("Ingrese el numero de muestras:"  + str(cont))
    
    KFmasa=float(input("Ingrese cantidad de masa:"))

    ARargon=float(input("Ingrese cantidad de argon:"))
    
#datos del proceso
    def calcular(KF, AR):
        
        edad=(1.248*10e9/math.log(2))*math.log((KF+AR/0.109)/KF)
               
        return edad

    result=calcular(KFmasa,ARargon)
    
    print("Cantidad de masa: ")
    print(KFmasa+ARargon)
    print("La edad aproximada es: ")
    print(result)
    print()
    if (result < 65.5):
            print("La era es Cenozoica")
    else:
            if result < 251:
                print("La era es Mezosoica")
            else:
                if result < 542:
                    print("La era es Palezoica")
                else:
                    print("La era es pre-Palezoica")

#datos de salida
