'''
Ejercicio 1

En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.
'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un pais para conocer su capital: ")
letra = pais.capitalize() in diccionario  
#la primer letra de la capital tiene que estar en Mayus para que lo reconozca el diccionario.

if letra == True:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario.")


'''
Ejercicio 2

Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número
'''

diccionario = {

    1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"

}

OpcionJugador = input("Ingrese el numero de jugador: ")

if OpcionJugador in diccionario:
    print(diccionario[OpcionJugador])
else:
    print("No es un numero dentro del diccionario. ")

#Opcion Jugador nos asegura que este dentro de diccionario. 