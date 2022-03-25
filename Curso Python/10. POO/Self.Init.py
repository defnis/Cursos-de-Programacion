#  Metodo Self

class FabricaTelefonos():
    marca = "Sangsung"

    def ElaborarHuawei(self): # Self viene por defecto. 
        self.marca = "Huawei" #Self sirve para engloba un atributo en una clase. 

telefono = FabricaTelefonos()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)


#////////////////////////////

#  Metodo Init

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color 

telefono = FabricaTelefonos('Huawei', "Negro")
print(telefono.marca)
print(telefono.color)

