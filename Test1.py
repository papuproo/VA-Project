import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Importando Datos
temperature_df = pd.read_csv("c_f.csv")

#Visualizacion
sns.scatterplot(temperature_df['Celsius'], temperature_df['Farenheit'])

#Cargando Set de Datos
x_train = temperature_df['Celsius']
y_train = temperature_df['Farenheit']

#Creando el modelo
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape = [1]))

model.summary()