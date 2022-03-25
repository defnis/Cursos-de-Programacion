class A():
    def __init__(self):
        self.cuenta = 0 
        self.contador = 0
    
    #Metodo Self
    @property  #Le decimos a python que llamo a un metodo GET. 
    def cuenta(self):
        return self._cuenta

    #Metodo Set. 
    @cuenta.setter  #Nombre del atributo + la palabra reservada setter.  
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador


a = A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)