class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color 
    
    def __srt__(self):
        return "El objeto es {}".format(self.marca)
        
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia", "Negro")
print(telefono.marca)
print(telefono)