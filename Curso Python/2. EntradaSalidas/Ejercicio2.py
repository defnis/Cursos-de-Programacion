'''  
Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''
vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

vocal = vocal.upper()
letra = letra.lower()

print("La letra es: {} \nLa vocal es: {}".format(letra,vocal))

'''
  Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>
'''

nombre = input("Como te llamas: ")
edad = int(input("Cuantos anios tenes: "))
sexo = input("Cual es tu sexo: ")

print("Tu nombre es {} tenes {} anios y tu sexo es {}".format(nombre,edad,sexo))