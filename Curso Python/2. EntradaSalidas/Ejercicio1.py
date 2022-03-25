'''  
Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''
from math import sqrt
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))
x1 = 0
x2 = 0

if((b**2)-(4*a*c))< 0:
    print("No se puede sacar raiz cuadrada ")
else:
    x1 = (-b +sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b -sqrt((b**2)-(4*a*c)))/(2*a)
    print("La solucion es: " "\nx1=",x1, "\nx2=",x2)


'''   
Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final
'''

practica1 = float(input("Ingrese la nota de la practica 1: "))
practica2 = float(input("Ingrese la nota de la practica 2: "))
practica3 = float(input("Ingrese la nota de la practica 3: "))
examenParcial = float(input("Ingrese el valor de del examen parcial: "))
examenFinal = float(input("Ingrese el valor del examen final: "))

promedio = (practica1 + practica2 + practica3)/3

promedioFinal = (promedio + 2*examenParcial + 3*examenFinal)/6

print("El promedio de practicas del estudiante es:\n ", promedio, "\n Y el promedio final es de:\n ", promedioFinal)
