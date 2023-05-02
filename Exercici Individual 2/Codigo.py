import json #Importamos la librería de json
import glob #Permite leer todos los archivos de la carpeta
import pandas as pd #Importamos la librería de pandas
from tqdm import tqdm #Mostrar el progreso de la acción en tiempo real

#creammos la variable que almacenará los datos con la función glob
files = glob.glob('twitter_api_responses/api_responses/*.json')

lista_dfs = [] #Creamos una lista que guardará toda la info
hashtags_all = [] #Creamos una lista para almacenar los hashtags
for file in tqdm(files): #For para abrir todos los archivos
    with open(file, 'r', encoding="utf-8") as jsonfile:
        datos = json.load(jsonfile) #Variable que almacena los tuits
        tweets = datos["data"] #Creamos una lista con todos los tweets del archivo
        users = datos["includes"]["users"] #agafem els usuaris

        for tweet in tweets:#pPor cada tuit cogemos el autor, dia, likes, retweet, reply e idioma
            author_id = tweet["author_id"]
            dia = tweet["created_at"]
            likes = tweet["public_metrics"]["like_count"]
            retweet = tweet["public_metrics"]["retweet_count"]
            reply=tweet['public_metrics']['reply_count']
            idioma= tweet["lang"]

            hashtags = [] #Creamos una lista
            if "entities" in tweet and "hashtags" in tweet["entities"]: #Condicional para saber el tuit tiene una key llamada hashtag
                hashtags = [hashtag["tag"] for hashtag in tweet["entities"]["hashtags"]] #Actualizamos la lista con los hashtags

            for hashtag in hashtags:
                hashtags_all.append({"tweet_id": tweet["id"], "hashtag": hashtag}) #Iteramos la lista hashtags y le añadimos un id y valor y lo añadimos a la lista vacía del principio


            for user in users: #iteramos para saber el nombre de usuario 
                if user["id"] == author_id:#Cogemos el nombre de usuario a partir del id anterior
                    username = user["username"] #Creamos la variable username               
                    followers_count = user["public_metrics"]["followers_count"] #Cogemos el número de followers del usuario                

                    # Creamos el dataframe con las columnas que queremos
            df = pd.DataFrame({
                "user_id":author_id,
                "username":username,
                "followers_count":followers_count,
                "text":tweet["text"],
                "created_at":dia,
                "like_count": likes,
                "reply": reply,
                "lang":idioma,
                "hashtags": hashtags,
                "retweet_count": retweet
            }, index=[0])
            lista_dfs.append(df) #Añadimos esto a la lista vacía del principio

df_final = pd.concat(lista_dfs) #Concatenamos todos los dataframes
df_final.to_csv("Part_A.csv", index=False) #Exportamos a csv 

lista_tuples = [] #Creamos una lista vacía
try: #Hacemos uso de la estructura try except para los casos en los que no haya la información que buscamos 
   lista_mencions = tweet["entities"]["mentions"] #creamos la lista de menciones
   for u in llista_mencions:#iteramos la lista
       mencionat = u["username"] #Extraemos el nombre de usuario
       tup = (username, mencionat) #Creamos una tupla que contiene el nombre de usuario y a quien menciona
       llista_tuples.append(tup) #Se añade la tupla a la lista fuera del try
except KeyError: #Si hay error pasamos
    pass
df = pd.DataFrame(lista_tuples, columns=['source', 'target'])#Creamos un DataFrame a partir de una lista de tuplas con las columnas Source y Target
df.to_csv("Part_B.csv") #Exportamos el dataframe a un csv
