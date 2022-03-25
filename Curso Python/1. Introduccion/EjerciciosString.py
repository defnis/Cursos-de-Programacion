'''
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: 
Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

cadena = "Te quiero solo como amigo"

print(cadena[0 : 2]) #Empieza en 0 y termina en 2. 
print(cadena[-3 : ]) #Empieza en -3 y ve hasta el final. 
print(cadena[: : 2]) #Va a imprimier cada 2 caracteres. 
print(cadena[: : -1]) #Va a imprimir de uno en uno a la inversa. 
print(cadena + cadena[ : : -1])
#Primero recorre la cadena y luego vuelve a la inversa. 


'''
Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0
'''

cadena = "S,e,p,a,r,a,d,o"

print(cadena[ : : 2])

# Uso del metodo Replace. Reemplaza un parametro que le indiquemos por otro. 

cadena1 = "Quiero regresar a las escuela maniana"
reemplaza = cadena1.replace("a", "A")

print(reemplaza)