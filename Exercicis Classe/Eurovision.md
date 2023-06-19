Pip install requests
``` Python
import requests

resposta = requests.get("https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_2023")

print (resposta.text)#imprimirà l'html de la pàgina que estem consultant

```
 El que obtinc és una espècie de paquet, un json/diccionari. 
-  pip install beautifulsoup4. Instalem la llibreria que serveix per a scrapejar 
- from bs4 import BeautifulSoup. Cridar el mòdul 
``` Python
import requests  
from bs4 import BeautifulSoup  
  
resposta = requests.get("https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_2023")  
  
print (resposta.text)#imprimirà l'html de la pàgina que estem consultant  
soup= BeautifulSoup(resposta.text,'html.parser') #El que fa es agafar la sopa i la parseja com un html
```

Volem buscar una taula dins d'aquesta sopa. Per localitzarla és inspeccionar al web i mirar la taula. Ho podem fer per la classe o dir-li que et doni totes les taules. 

``` Python
import requests  
from bs4 import BeautifulSoup  
  
resposta = requests.get("https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_2023")  
  
print (resposta.text)#imprimirà l'html de la pàgina que estem consultant  
soup= BeautifulSoup(resposta.text,'html.parser') #El que fa es agafar la sopa i la parseja com un html  
  
taules = soup.find_all("table")  
  
#Ara volem imprimir totes les taules en un dataframe  
for taula in taules:  
    df = pd.read_html(taula)  
    print(taula)
```

El que farà això és dir-nos quina posició de taula ocupa la taula que volem a la web, el que passa és que cada any 

``` Python
import requests  
from bs4 import BeautifulSoup  
import pandas as pd  
  
anys = range(2000, 2023, 1) # El que fa és anar d'any a any indicats, per cada número que indiquem  
  
for any in anys:  
    resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_2023{any}")  
    soup= BeautifulSoup(resposta.text,'html.parser') #El que fa es agafar la sopa i la parseja com un html  
    taules = soup.find_all("table")  
    final= soup.find('span',id='final')  
    tabla = final.find_next("table")  
    df = pd.read_html(tabla.pretify())  
    print(df)
```

```` Python
#pip install lxml  
  
import pandas as pd  
import requests  
from bs4 import BeautifulSoup  
  
anys = range(2000, 2024, 1) # El que fa és anar d'any a any indicats, per cada número que indiquem  
  
llista_dataframes = []  
for any in anys:  
    try:  
        resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{any}")  
        soup= BeautifulSoup(resposta.text,'html.parser') #El que fa es agafar la sopa i la parseja com un html  
        taules = soup.find_all("table")  
        final= soup.find('span',id='Final')  
        tabla = final.find_next("table")  
        df = pd.read_html(tabla.prettify())[0]#Prettify és una variable de pandas que fa que es quedi maco  
        df["any"] = any  
  
        df.columns.values[0] = "N."  
        df.columns.values[5] = "Puntos"  
        df.columns.values[2] = "Cantante"  
        print(df)  
        llista_dataframes.append(df)  
    except AttributeError:  
        print(f"error: {any}")  
  
final= pd.concat(llista_dataframes)  
final.to_excel("llista_final.xlsx",index=False)
```
