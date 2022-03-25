''' 
Clases: Una clase es una entidad que define una serie de elementos que determinan un estado es decir datos y un comportamiento es decir operaciones sobre la los datos que modifican su estado.

class Galleta()

Objetos: Es simplemente un trozo de código más estructura de datos, más pequeño que un programa completo. 

galleta = Galleta()

La clase es como un molde que sirve para todas las galletas, los objetos son las caracteristicas de cada galleta.
'''

class FabricaTelefonos():
    pass 

print(type(FabricaTelefonos()))
#Nos devuelve en la terminal que es de tipo clase. 

celular = FabricaTelefonos()
print(type(celular))
#Clase main, es un objeto de la FabricaTelefonos. 
celular2 = FabricaTelefonos()
# Se puede crear tantos objetos como se quieran.  

def FabricaTelefonos():  
    pass  
# Aca se esta creando una funcion.   