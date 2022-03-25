'''
Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
'''

lista = [20, 50, "Curso", 'Python', 3.14]
print("Estos son los valores de la lista: ", lista)

palabra1 = input("Ingrese el valor de la primer palabra: ")
palabra2 = input("Ingrese el valor de la palabra dos: ")

lista[0] = palabra1
lista[1] = palabra2
print(lista)

'''  
Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos.
'''

lista = [1,2,3,4,5,6,7,8,9,10]

lista[3] *= 2
lista[6] *= 2
lista[9] *= 2

print(lista)