conjunto = {1,2,3,4,5,6}
# Dentro de un conjunto puede haber ()  {}  []  ... 

#En el conjunto no se puede repetir valores.  

conjunto.add(20)  #Agrega un elemento.  
print(conjunto)

conjunto.remove(1)   #Se remueve un elemento. 
print(conjunto)

conjunto.pop()  #Elimina el ultimo
print(conjunto) 

conjunto.update([1,8,9])  #Agrega elemento iterable.  
print(conjunto)

conjunto.clear()  #Vacia el conjunto.
print(conjunto)