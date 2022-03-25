# Las cadenas de texto (string) cuentan los espacios vacios.
'''
"Monty Python"

[0:4]="Monty"  Muestra las primero 5 letras.
[ :3]="Mon"    Muestra las primeras 3 letras.
[3: ]="hon"    Muestra las ultimas 3 letras.   '''

print ("Hola Mundo")

cadena = "Esto es un ejemplo de cadenas de tecto"
print(cadena)

# Escapar caracteres, String litera. 

cadena1 = "Esto es un \"ejemplo\" de escapar caracteres"
print(cadena1) #Marca "c" en las palabras marcadas. 

cadena2 = "Esto es un \nejemplo de escapar caracteres"
print(cadena2)  #Salto de linea. 

nombre1 = " Jose"
nombre2 = " Waiman"

print("Hola" + nombre1 + nombre2)
