class A():
    def __init__(self, contador, cuenta):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador 

a = A()
# No es una buena practica de programacion. 
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
    
# Cuando utilizas _ es para encapsular. 