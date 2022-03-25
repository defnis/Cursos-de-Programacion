
''' 
Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

palabra1 = input("Escriba la primer palabra: ")
palabra2 = input("Escriba la segunda palabra: ")

letras = palabra1[ -3: ]
letras1 = palabra2[ -3: ]
print(letras, letras1)


if (letras == letras1):
    print("Las 3 ultimas letras riman")
elif palabra1[-2: ] == palabra2[-2: ]:
    print("Las ultimas dos letras coinciden")
else:
    print("Las palabras no riman.")
        
    
'''  
Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula.
'''

opcion = input("Ingresa la opcion de tu Candidato: ")

if opcion.upper() == "A":
    print("Usted eligio el candidato Rojo")
elif opcion.upper() == "B":
    print("Usted escogio al candidato Verde")
elif opcion.upper() == "C":
    print("Usted escogio el candidato Azul")
else:
    print("La letra es uno opcion erronea, eliga A, B o C.")