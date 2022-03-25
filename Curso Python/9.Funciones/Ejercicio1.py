'''        
Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''
lista = []
num = 0

def pedir():
    i = 0
    while i <= 5: #Nos va a pedir 5 numero para ordenar.  
        num = float(input("Ingresa un numero: "))
        list.append(num) # Se agrega a la lista.
        i += 1    # Agrega uno y vuelve a pedir.  

def ordenar():
    lista.sort = []
    pares = []
    inpares = []
    for i in lista:  # Pide 5 numeros, si es divisivle por 2 es par.  
        if i % 2 == 0:
            pares.append(i)  # Par si el residio de la division es 0.  
        else:
            inpares.append(i)  
    print(pares)
    print(inpares)

    pedir()
    ordenar()


