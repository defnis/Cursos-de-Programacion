class A():
    def __init__(self):
        self.cuenta = 0 
        self.contador = 0
    
    @property  #Le decimos a python que llamo a un metodo GET. 
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador


a = A()
print(a.cuenta)
print(a.contador)