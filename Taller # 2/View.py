#definicion de la clase
class DepartamentoView:

    
    def __init__(self):
        self.breakliner = "***********************************"

    def welcome(self):
        print(self.breakliner+'\n'+"Bienvenidos a la Tienda")
        print(self.breakliner+'\n'+ "Ingrese los datos que se le solicitan")

    def goodbye(self):
        print('\n'+self.breakliner+"Muchas gracias ")

    def ver_departamento(self, departamento):
        print(self.breakliner+'\n'+ departamento.cod + departamento.nombre)

    def ver_producto(self, producto):
         print(self.breakliner+'\n'+ producto.descrip + producto.precio)

    def ver_descuento(self, descuento):
         print(self.breakliner+'\n'+ descuento.porc + descuento.duracion)

    def mensaje(self,mensaje):
        print(mensaje+'\n')

