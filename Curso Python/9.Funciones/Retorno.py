
def entero():
    print("Este es un numero entero: ")
    return 10

def decimal():
    print("Este es un dato decimal: ")
    return 90.99 

def frase():
    print("Jose Waiman")

def asignacion():
    return 1, 2, 3, 4, 5


print(entero()) # A los retornos hay que ponerle la palabra print. 
print(decimal())
print(frase())

# Se asignan valores a las variables.  
a, b, c, d, e = asignacion()
print(a)