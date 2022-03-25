'''   
Ejercicio 2

Escribir una función que reciba una muestra de números en una tupla y devuelva su medida.
'''  

def medida(*tupla):
    print(len(tupla))

medida(2, 3, 4, 19, 23)

#/////////////////////////

def medida(*tupla):
    return(len(tupla))

print (medida(2, 3, 4, 19, 23))

#///////////////////////////