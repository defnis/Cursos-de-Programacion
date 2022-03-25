class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje 

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago wow!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Yo hago Guaua")
perro.hablar()

pez = Pez("Nan")
pez.hablar()