'''       
Atributos: Son características cualidades o descripciones que los objetos tienen aunque desde un punto de vista de código en realidad son datos que tienen los objetos por ejemplo color santa marca son los datos de un auto características de un auto.

class Automovil():
    color
    llantas
    marca


Metodos: Son funciones pero que en P o o pasan a llamarse métodos los cuales hacen los objetos por ejemplo si una clase creo objetos personas entonces su método puede ser hablar escribir cantar.

class Personal(): # Clase
    def Hablar():  # Funcion
        print("Hola")
'''

class FabricaTelefonos():
    marca = "Huawei"
    color = "negro"
    memoria = 32
    almacemamiento = 128

    def llamar(self, mensaje):  #Metodo de instancia. 
        return mensaje 
    
    def escucharMusica (self):
        print("Estas escuchando musica.")


telefono = FabricaTelefonos()
telefono.marca    # Son variables dentro de una clase, son atributos. 
telefono.color

print(telefono.llamar("Hola, con quien hablo?"))
telefono.escucharMusica()