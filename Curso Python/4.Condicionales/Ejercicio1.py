'''  
Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''
letra = input("Ingresa una letra: ")

if letra.lower() == "aeiou":  #Es una manera de concatenar las vocales. 
    print("Es una vocal")
else:
    print("No es una local")

'''  
Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
'''

numero = int(input("Ingrese el numero Entero: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: {}".format(numero, abs(numero)))