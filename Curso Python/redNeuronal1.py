import tensorflow as tf  
import numpy as np  

celsius =np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, -20, 13, 32, 46, 67, 70], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])