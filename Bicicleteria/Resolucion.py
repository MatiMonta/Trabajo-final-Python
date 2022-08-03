class Bicicleteria:
 #Atributos
    def __init__(self, bicicletas, ganancias, cantidad_de_ventas):
        self.bicicletas = bicicletas
        self.ganancias = ganancias
        self.cantidad_de_ventas = cantidad_de_ventas
#Metodos
    def ver_bicicleteria(self):
        print("Bicicletas",self.bicicletas)
        print("Ganancias",self.ganancias)
        print("Cantidad de Ventas", self.cantidad_de_ventas)

    def vender_bicicleta(self,ganancias,cantidad_de_ventas):
        self.ganancias=self.ganancias+ganancias
        self.cantidad_de_ventas= self.cantidad_de_ventas + cantidad_de_ventas

    def comprar_bicicleta(self,bicicletas):
        self.bicicletas=self.bicicletas+ bicicletas

bicicleteria1=Bicicleteria(20,0,0)
bicicleteria1.comprar_bicicleta(2)
bicicleteria1.vender_bicicleta(55000,1)
bicicleteria1.ver_bicicleteria()


class Bicicleta:
#Atributos
    def __init__(self, nro_de_serie,modelo,anio,precio):     
        self.nro_de_serie=nro_de_serie
        self.modelo=modelo
        self.anio=anio
        self.precio=precio
    def ver_bicicleta(self):
        print("Nro de serie: ",self.nro_de_serie," - ", "Modelo: ",self.modelo," - ","Año: ",self.anio," - ","Precio: ",self.precio)
#Metodos
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio=precio
    def getNro_de_serie(self):
        return self.nro_de_serie


bici1=Bicicleta("A65585","OVER",2020,55000)
bici1.ver_bicicleta()
bici2=Bicicleta("A65586","ASUS",2021,35000)
bici2.ver_bicicleta()
bici3=Bicicleta("A65587","ROVER",2022,88000)
bici3.ver_bicicleta()
bici4=Bicicleta("A65588","GILERA",2022,100000)
bici4.ver_bicicleta()