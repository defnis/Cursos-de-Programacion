''''
Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

Generar un DataFrame con los datos de los cuatro ficheros.
Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones, contaminantes y fecha.
Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
Mostrar un resumen descriptivo (mímino, máximo, media, etc) para cada contaminante.
Mostrar un resumen descriptivo para cada contaminente por distritos.
Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estadión indicada.
Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.
'''

import pandas as pd
import numpy as np
import datetime as dt

# Generar un DataFrame con los datos de los cuatro ficheros
import pandas as pd 

emisiones_2016 = pd.read_csv('emisiones-2016.csv', sep = ';')
emisiones_2017 = pd.read_csv('emisiones-2017.csv', sep = ';')
emisiones_2018 = pd.read_csv('emisiones-2018.csv', sep = ';')
emisiones_2019 = pd.read_csv('emisiones-2019.csv', sep = ';')
emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])
emisiones


