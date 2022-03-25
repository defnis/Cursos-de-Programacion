'''   
Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
for i in range(1,11):
    print(i) 

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese otro valor:"))

for i in range(num1, num2 +1):
    print(i)


'''
Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''   

num4 = int(input("Ingrese primer numero: "))
num5 = int(input("Ingrese el segundo numero: "))

for i in range(num4, num5):
    if i % 2 == 0: #Los que divide por 2, los elimino. No los muestro. 
        continue
    print(i)