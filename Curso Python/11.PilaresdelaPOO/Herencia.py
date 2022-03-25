class Animales ():
    def habla(self):
        print("Yo soy un animal")
    def descripcion(self):
        print("Yo soy un {}".format(self.animal))


#Los metodos y atributos que tenga la clase Animales las hereda perro.   
class Perro(Animales): #
    pass   #No vamos a colocar nada, ningun metodo.

class Abeja (Animales):
    def __init__(self, animal):
        self.animal = animal 

animal = Animales()
animal.habla()

perro = Perro()
perro.habla() 
#Como vamos a llamar un metodo que no tenemos, es porque lo hereda de la clase animal. 

abeja = Abeja("Abeja")
abeja.descripcion()