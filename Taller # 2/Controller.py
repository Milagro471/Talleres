from Model import Departamento
from Model import Producto
from Model import Descuento
from View import DepartamentoView


from os import system, name 

class Controller:

    def __init__(self):
        # init construct
       
        self._lista_departamento = [] # creacion de la  lista 
        self._lista_productos = [] 
        self._lista_descuento = [ ]
        self.View = DepartamentoView() 
        self.View.welcome() 


  #metodos de agregar

    def agregarDepartamento(self, Departamento):

        self._lista_departamento.append(Departamento)

    def agregarProducto(self,Producto): 
        
        self._lista_productos.append(Producto)

    def agregarDescuento(self,Descuento): 
        
        self._lista_descuento.append(Descuento)


#metodo de actualizar


    def actualizar_ViewDepartamento(self): 
        
        self.View.mensaje("LISTA DE DEPARTAMENTOS: "+ str(len(self._lista_departamento))) 
        

        if len(self._lista_departamento)==0: # si la lista esta vacia
            self.View.mensaje("No se ha ingresado ningun departamento aún!") 

        else: 
            for Departamento in self._lista_departamento: 
                self.View.ver_departamento(Departamento) 

    def actualizar_ViewProducto(self): 
        
        self.View.mensaje("LISTA DE PRODUCTOS: "+ str(len(self._lista_productos))) 
        

        if len(self._lista_productos)==0: # si la lista esta vacia
            self.View.mensaje("No se han ingresado ningún producto!") 

        else: 
            for Producto in self._lista_productos: 
                self.View.ver_producto(Producto) 


     def actualizar_ViewDescuento(self):
 
        self.View.mensaje("LISTA DE DESCUENTOS: "+ str(len(self._lista_descuento))) 
        

        if len(self._lista_descuento)==0: # si la lista esta vacia
            self.View.mensaje("No se ha ingresado ningun descuento aun!") 

        else: 
            for Descuento in self._lista_descuento: 
                self.View.ver_descuento(Descuento) 


    def stopProgram(self): # llama a la vista 
        self.View.goodbye() 

    def cleanTerminal(self):
        
        if name == 'nt': 
            _ = system('cls') 
    
       
        else: 
            _ = system('clear') 


    def agregar(self): 
        # metodo del controller para solicitar datos e ingresar nuevo producto
        try:
            userInput = str(input("Desea agregar algún dato al Controller? Y/N")) 
        

            if userInput=='Y':

                _lista_departamento = input("Ingrese el codigo, el nombre separado por coma-> Cod,Nombre [Sin espacios al inicio]: ").split(',') 
                Departamento_nuevo = Departamento(datos_newDepartamento[0], datos_newDepartamento[1]) 
            
                self.agregarDepartamento(Departamento_nuevo)

                 _lista_productos = input("Ingrese la descripcion, el precio por coma-> descrip, precio [Sin espacios al inicio]: ").split(',') 
                Producto_nuevo = Producto(datos_newProducto[0], datos_newProducto[1]) 
            
                self.agregarProducto(Producto_nuevo)

                 _lista_descuento = input("Ingrese el porcentaje, l duracion por coma-> porc, duracion [Sin espacios al inicio]: ").split(',') 
                Descuento_nuevo = Descuento(datos_newDescuento[0], datos_newDescuento[1]) 
            
                self.agregarDescuento(Descuento_nuevo)
                               
 
        except:
            # para capturar errores
            self.View.mensaje("Error en la entrada del usuario") 


    def run(self):
        
        
        corriendo = True
        userInput = None

        while corriendo == True:
            try: # loop que ejecuta el programa
                if userInput==None:
                    userInput = input("Y to display list and continue /N to exit /O for more options: ")
                if userInput == 'Y':
                    self.actualizar_ViewDepartamento() 
                    self.actualizar_ViewProducto()
                    self.actualizar_ViewDescuento()
                    userInput = input("Y to display list and continue /N to exit /O for more options: ")
                elif userInput=='N':
                    self.stopProgram()
                    corriendo=False
                else:
                    self.agregarDepartamento() 
                    self.agregarProducto()
                    self.agregarDescuento()
                    self.actualizar_ViewDepartamento() 
                    self.actualizar_ViewProducto()
                    self.actualizar_ViewDescuento()
                    self.View.mensaje("Gracias por utilizar -- Re-starting.../// (...loading...)")
                    userInput = input("Desea volver a utilizarlo? Y to continue /N to exit: ")
                    self.cleanTerminal()
            except:
                self.View.mensaje("Error en la entrada del usuario")


# metodo main
if __name__=="__main__":
    control= Controller()
    control.run()
                    

