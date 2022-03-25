''''
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
'''

import pandas as pd 
import matplotlib.pyplot as plt 

# Creamos un dataframe a partir del fichero csv
df_titanic = pd.read_csv('titanic.csv')
# Creamos la figura y los ejes
fig, ax = plt.subplots()
# Diagrama de sectores de falleccidos y supervivientes
df_titanic.Survived.value_counts().plot(kind = "pie", labels = ["Muertos", "Supervivientes"], title = "Distribución de supervivientes")
plt.show()