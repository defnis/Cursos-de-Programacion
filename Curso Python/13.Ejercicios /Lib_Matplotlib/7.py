''''
El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.
'''

import pandas as pd 
import matplotlib.pyplot as plt 

def evolucion_cotizacion(datos, variable):
    '''Función que construye un diagrama de lineas con la evolución de las cotizaciones de las empresas en bolsa.
    
    Parámetros:
        - datos: Es un dataframe de Pandas con las columnas Empresa, Apertura, Mínimo, Máximo, Cierre, Volumen.
        - variable: Es una cadena con el nombre de la columna del dataframe a dibujar.

    Salida:
        Un gráfico de líneas con las series temporales de las cotizaciones de cierre de cada empresa.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de cotizaciones por empresa
    datos.groupby('Empresa').plot(x = 'Fecha', y = variable, ax = ax)
    # Añadimos el título
    plt.title('Evolución de las cotizaciones (' + variable + ')')
    # Añadimos la legenda
    plt.legend(df_datos.groupby('Empresa').groups.keys())
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

# Creamos un dataframe a partir del fichero csv
df_datos = pd.read_csv('bancos.csv')
# Convertimos la columna Fecha a formato datetime
df_datos["Fecha"] = pd.to_datetime(df_datos["Fecha"])
# Llamamos a la función para crear el gráfico
evolucion_cotizacion(df_datos, 'Cierre')
plt.show()