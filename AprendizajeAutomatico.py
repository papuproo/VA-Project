# Conseguir código del profe relacionado al análisis de datos de Iris

# ... Aquí hay código que define la variable X y la variable Y así como la función para calcular el porcentaje de error
#X = dataX[0:150,[0,1,2,3]]

# Vamos a crear el clasificador/regresión, recuerden que debemos tener el archivo .csv de Iris

clasificador = sk.svm.SVC(kernel = "lienal")
clasificador.fit(X,Y)
predicciones = clasificador.predict(X)
# Tenemos fit que entrena y predict pues produce