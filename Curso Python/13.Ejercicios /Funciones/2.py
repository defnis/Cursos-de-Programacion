'''      
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
'''

def greet(nombre):
    """Función que muestra un saludo por pantalla.
    Parámetros
    nombre: Nombre del usuario
    Devuelve el saludo ¡Hola nombre!.
    """
    print('¡Hola ' + nombre +'!')
    return

greet('Alf')
greet('Python')