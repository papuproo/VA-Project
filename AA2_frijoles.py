import numpy as np
from sklearn.svm import SVC 
from sklearn.cluster import KMeans

queClase={
    1:"Seker",
    2:"Barbunya",
    3:"Bombay",
    4:"Cali",
    5:"Dermosan",
    6:"Horoz" ,
    7:"Sira"
}

datos = np.genfromtxt("frijoles.csv",dtype=float,delimiter=",")

atributos = datos[:,:-1]
clase = datos[:,-1]  

a = (0,2026)
b = (2026,3348)
c = (3348,3870)
d = (3870,5500)
e = (5500,7428)
f = (7428, 10064)
g = (10064,13611)

def entrenaKM(atributos):
    clusterizador = KMeans(n_clusters=7,tol=1e-15,max_iter=10000000)
    clusterizador.fit(atributos)
    return clusterizador

def entrenaSVC(atributos,clase):
    clasificador = SVC(kernel='linear', C=1.0, random_state=42)
    clasificador.fit(atributos, clase)
    predicciones = clasificador.predict(atributos)
    return predicciones,clasificador

#predicciones = entrena()

def pruebaSVC(predicciones,clase):
    buenos = 0
    for c in range(13611):
        # print(queClase[clases])
        if (predicciones[c]==clase[c]):
            buenos += 1
    print("El porcentaje de aciertos es: ",buenos/len(clase)*100,"%")

def conteoP(prediccion,rango):
    porc = 0
    frec = [0,0,0,0,0,0,0]
    for i in range(rango[0],rango[1]):
        frec[prediccion[i]]+=1
    porc=max(frec)/(rango[1]-rango[0])*100
    return [frec,porc]

def imprimeBonito(Lista):
    #print(Lista[0],Lista[0].index(max(Lista[0])))
    print("El porcentaje de este frijol es: ",Lista[1],"%")
   
clusterizador = entrenaKM(atributos)
prediccion=clusterizador.predict(atributos)    
#predicciones = entrena(atributos,clase)
#prueba(predicciones,clase)
imprimeBonito(conteoP(prediccion,a))
imprimeBonito(conteoP(prediccion,b))
imprimeBonito(conteoP(prediccion,c))
imprimeBonito(conteoP(prediccion,d))
imprimeBonito(conteoP(prediccion,e))
imprimeBonito(conteoP(prediccion,f))
imprimeBonito(conteoP(prediccion,g))
