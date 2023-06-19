
El que es fa es llegir tots els datasets a l'hora. 

``` Python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*")  
  
for data in datasets:  
    df = pd.read_csv(data)

```

Al llegir el dataset li hem d'indicar el separador 
``` Python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*")  
  
for data in datasets:  
    df = pd.read_csv(data,sep="\t") #Indiquem el separador de columnes

```

En cas de voler extraure només la informació d'un streamer usarem el següent codi
``` Python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*") 

llista = []

llista_streamers = ["auronplay","Illojuan"]
  
for data in datasets:  
    df = pd.read_csv(data,sep="\t")
    df.loc[df['streamer_name']=="auronplay"]
	llista.append(df) #Creem una llista per només afegir dades d'auronplay

df_final=pd.concat(llista) #Concatenem i igualem a una variable
df_final.to_csv(f"{streamer}-dataset.csv",index=False)

```

Ho volem fer per 2 streamers i amb el codi anterior només ho estem fent per 1 d'ells. Cal crear un altre for. 
``` Python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*") 

llista = []

llista_streamers = ["auronplay","Illojuan"]
  
for data in datasets:  
    df = pd.read_csv(data,sep="\t")
    for streamer in llista_streamers:
        df.loc[df['streamer_name']=="auronplay"]
		llista.append(df) 

df_final=pd.concat(llista) 
df_final.to_csv(f"{streamer}-dataset.csv",index=False)

```

El que caldria fer es generar una llista dinàmica. 
``` Python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*") 

llista = []

llista_streamers = ["auronplay","Illojuan"]
  
for data in datasets:  
    df = pd.read_csv(data,sep="\t")
    for streamer in llista_streamers:
        df_2=df[df['streamer_name']=="auronplay"]#Així millor
		llista.append(df_2) 

df_final=pd.concat(llista) 
df_final.to_csv(f"{streamer}-dataset.csv",index=False)

```

## Analitzant l'arxiu JSON de Twitter

Gràcies a la Intel·ligència artificial twitter és capaç de saber qui es la persona a la que es cita o la persona qui tuiteja.
és interessant saber si és un quote o no. Importància a la tipologia. 
Haurem de fer un Try al referenced_tweet. En cas que doni error etiquetar com a tuit pur. 

- Includes conté una llista d'usuaris.  A l'ID de l'usuari i del nom. Quan processem cadascun dels tuits hem de processar el ID i buscam l'ID i indicar a quin name correspon.

