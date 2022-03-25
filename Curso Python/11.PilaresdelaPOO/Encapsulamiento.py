# Encapsular es para contener la informacion y ahorro de memoria.

class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

print("Objero 1")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

print("Objero 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
#print(b.__contador)  # __ Significa encapsulamiento pero no es la mas optima. Encapsular es para los atributos.  