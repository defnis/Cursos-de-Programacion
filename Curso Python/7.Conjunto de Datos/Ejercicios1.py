'''
Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''
tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",  "Octubre", "Novienbre", "Dicimebre")

mes = int(input("Ingrese el numero del mes: "))
mes -= 1
print(tupla[mes])
# Cuando el usuario selecciones el numero, se le va a restar uno.abs(x)
'''  
Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa   
'''
anio = ("a","b", "c", "d","e","f","g","h","i","j","k","l")

anio = int(input("Ingrese el numero del mes: "))
anio -= 1
print(tupla[anio])