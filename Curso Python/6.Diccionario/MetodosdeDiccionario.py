diccionario = {1:2, 2:3, 3:4}
diccionario2 = {4:5, 5:7}
print(diccionario)

diccionario.clear() # Borra el diccionario.  
print(diccionario)

diccionario.get(2) #Solo muestra la 2da llave.  
print(diccionario)

diccionario.setdefault(4,5)
print(diccionario)

diccionario.update(diccionario2)
print(diccionario)

diccionario.copy()
print(diccionario)