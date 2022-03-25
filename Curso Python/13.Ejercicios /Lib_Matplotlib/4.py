''''
Escribir una función que reciba una serie de Pandas con el número de ventas de un producto durante los meses de un trimestre y un título y cree un diagrama de sectores con las ventas en formato png con el titulo dado. El diagrama debe guardarse en un fichero con formato png y el título dado.
'''

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_sectores_ventas(ventas, titulo):
    '''Función que construye un diagrama de sectores con las ventas de un trimestre y lo guarda con un nombre dado. 
    
    Parámetros:
        - ventas: Es una serie de Pandas con las ventas del trimestre, siendo el índice los meses.
        - titulo: Es una cadena con el título.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos los sectores con las verntas a partir de la serie
    ventas.plot(kind = 'pie', ax = ax)
    # Eliminamos el título del eje y
    plt.ylabel('')
    # Añadimos el título
    plt.title(titulo)
    # Guardamos el gráfico con el nombre dado en formato png
    plt.savefig(titulo + '.png')
    return 

ventas = {'Enero':200, 'Febrero':240, 'Marzo':310}
s_ventas = pd.Series(ventas)
diagrama_sectores_ventas(s_ventas, 'Ventas primer trimestre')