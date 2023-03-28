## Api Twitch

Twitch té molts servidors que sustenten una base de dades. L'api té definits qué pots agafar i qué no. Regula l'entrada i la sortida de dades constantment. No hi ha relació directe entre l'usuari i la base de dades. Per fer una solicitud  a l'api hi ha dos vies: 
- Solucions complexes per a desenvolupadors. 
- Hi ha gent que ha facilitat una llibreria de python. 

A continuació enganxarem el següent text per importar l'API


``` Python
from twitchAPI.twitch import Twitch #Importa la seva llibreria

twitch = Twitch('my_app_key', 'my_app_secret') #Això dins de la pàgina de desenvolupadors de twitch posar primer la ID i després li donem a nuevo secreto
pprint(twitch.get_users(logins=['your_twitch_username']))
```


## Funcions recursives

Una funció recursiva és una funció que s'utilitzará més tard
```Python
variable = "hola"

def loquesea(variable):
	print(variable)

loquesea(variable)


```

A python li dona igual com es digui la variable dins de la funció. 
Dummy Variables

Try és intenta, i si no pots

Còpia del exercici al Python, cal comentar-ho

``` python
from twitchAPI.twitch import Twitch #Carrega la seva llibreria  
import datetime #per importar a l'hora en que hem llançat l'escript  
#import json  
import pandas as pd #La importem perque ens permeti fer el data frame  
import time  
  
  
now =datetime.datetime.now() #aquesta funció serveix per mostrar l'hora de petició  
twitch = Twitch('xxxx', 'xxxx') #Li dono les credencials  
  
llista_dataframes = [] #treiem aquest element de la llista perquè sino es maxacarà  
cursor_dummy = None #Quan la api rep que el cursor es None sap que és la primera pàgina  
  
def crida(cursor):  
  
    '''streams = twitch.get_streams(first=20, language= "es") #Agafem els primers 20 directes en idioma espanyol  
    print(streams) #Ens crea diccionaris    '''    '''data = streams["data"] #Una llista de coses  
  
    for d in data:        print(d)'''    streams = twitch.get_streams(first=20, language="ca",after=cursor)  # Agafo només el primer directe i l'emmagatzemo a streams, L'after demana una nova petició  
    '''with open("output_file.json", 'w', encoding='utf-8') as f:  
        json.dump(streams, f, ensure_ascii=False, indent=4) això ens ho carreguem perque ja no volem crear cap arxiu json    '''    dades = streams["data"]  # La data és tot  
    cursor = streams["pagination"]["cursor"]  
  
    for dada in dades:  
        captured_at = now  
        user_id = dada["user_id"]  
        user_name = dada["user_name"]  
        game_id = dada["game_id"]  
        game_name = dada["game_name"]  
        title = dada["title"]  
        viewer_count = dada["viewer_count"]  
        started_at = dada["started_at"]  
        is_mature = dada["is_mature"]  
  
        df = pd.DataFrame({  
            "captured_at": captured_at,  
            "user_id": user_id,  
            "user_name": user_name,  
            "game_id": game_id,  
            "game_name": game_name,  
            "title": title,  
            "viewer_count": viewer_count,  
            "started_at": started_at,  
            "is_mature": is_mature,  
  
        }, index=[0])  # per indicar a Pandas l'index de la primera fila, que és 0  
        llista_dataframes.append(df)  
  
        #Ara intentem agafar el cursor per a la següent pàgina  
        try:  
            cursor= streams["pagination"]["cursor"]  
            print(cursor)  
            print(f"Fent una nova consulta. Total de streams: {len(llista_dataframes)}")  
            time.sleep(0.12)
