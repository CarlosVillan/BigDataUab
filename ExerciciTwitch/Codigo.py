import pandas as pd #Importamos la librería de Pandas

#Leemos el archivo del dataset csv y le especificamos el separador de columnas y las columnas que usaremos
df = pd.read_csv("feb_23_es_simple.csv",sep="\t", usecols=["streamer_name","game_name","viewer_count","captured_at"])

#1. ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?
df1 = df.groupby("captured_at")["viewer_count"].sum().reset_index() #Agrupamos los datos por la columna 'captured_at', calculamos la suma de la columna 'viewer_count' para cada grupo y reseteamos los índices de las filas
df1.to_csv("1_evolucion_views.csv") #Exportamos el dataframe a un archivo csv

#2.¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?
df2 = df.groupby("game_name").agg({'viewer_count': ['sum', 'count']}).reset_index() #Agrupamos el dataset por la columna 'game_name' y se agrega mediante la función .agg() las operaciones de suma y conteo de los viewers
df2.columns = ['game_name', 'viewer count', 'capturas'] #Renombramos las columnas
df2.to_csv('2_cat_vistas_hrs.csv', index=False) #Exportamos el dataframe a un archivo csv quitando el índice

#3¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?
df3=df.groupby(["captured_at","game_name"])["viewer_count"].sum().reset_index() #Agrupamos los datos por las columnas 'captured_at' y 'game_name', calculamos la suma de la columna 'viewer_count' para cada grupo y reseteamos los índices de las filas
df3.to_csv("3_evolucion_cat.csv") #Exportamos el dataframe a un archivo csv

#4 ¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?
df4 = df.groupby('streamer_name')['viewer_count'].agg({'sum', 'count'}).reset_index() #Agrupamos el dataset por la columna 'streamer_name' y se agrega mediante la función .agg() las operaciones de suma y conteo de los viewers
df4.columns = ['streamer_name', 'viewer_count', 'captured_at'] #Renombramos las columnas
df4.to_csv('4_distr_streamers.csv', index=False)#Exportamos el dataframe a un archivo csv quitando el índice

#5¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?
df5 = df.groupby("captured_at").agg(desviacion=("viewer_count", "std")).reset_index()#Realizamos el cálculo de la desviación estándar de la columna 'viewer_count', usando el parámetro 'std' agrupando los valores a la columna 'Captured_at'y reseteamos los índices de las filas
df5.to_csv("5_desviacion.csv", index=False, decimal=",")#Exportamos el dataframe a un archivo csv quitando el índice y especificando que se debe usar el separador decimal en lugar del punto
