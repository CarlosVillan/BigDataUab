
https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items

Pip install spotipy - instalem la llibrería

Cada vegada que es fa una petició a l'API, va el que estem demanant però també els nostres codis d'autentificació. 
Copiem el codi que ens dona l'API.

```Python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='xxxx'  
SPOTIPY_CLIENT_SECRET='xxxx'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = sp.user_playlists('spotify')  
while playlists:  
    for i, playlist in enumerate(playlists['items']):  
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))  
    if playlists['next']:  
        playlists = sp.next(playlists)  
    else:  
        playlists = None
```
Ara ho matem. Per fer el que necessitem és obtenir les cançons d'una playlist nostre

``` Python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
import json  
  
SPOTIPY_CLIENT_ID='xxxx'  
SPOTIPY_CLIENT_SECRET='xxxx'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist = "3oopyXIZGLFtHjFYN9KbuI"  
  
#https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  
  
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None) #Sp. per imprimir les credencials  
  
print(query)  
  
with open('hola.json', 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)
```

El que hem fet ha sigut crear un arxiu json amb la resposta d'agafar els items de la playlist.

``` Python  
for i in query["items"]:  
    print(i)
```

Ara iterem la query perque volem esbrinar quins artistes hi ha i quina id tenen

``` Python
for i in query["items"]:  
    artists = i["track"]["artists"] #Al ser una llista i no un claudàtor hem d'iterar tots els elements  
    for artist in artists:  
        artist_name = artist["name"]  
        artist_id = artist["id"]  
        print(artist_name,artist_id)
```

Per cada artista de la playlist agafa la ID i per cada un agafem artistes relacionats
``` Python
for i in query["items"]:  
    artists = i["track"]["artists"] #Al ser una llista i no un claudàtor hem d'iterar tots els elements  
    for artist in artists:  
        artist_name = artist["name"]  
        artist_id = artist["id"]  
        print(artist_name,artist_id)  
          
          
        related_artist = sp.artist_related_artist(artist_id) #funció per esbrinar els artistes recomanats  
  
        with open(f'{artist_id}hola.json', 'w', encoding='utf-8') as f: #Per cada artist id, crearà un arxiu json d'artistes relacionats  
            json.dump(related_artist, f, ensure_ascii=False, indent=4)
```

Ara hem afegit l'import time per refrescar a cada petició 1 segon  l'API i no saturar-la
```Python
time.sleep(1) 
```

## Llistar totes les relacions d'artistes relacionats

El tamany del node vindrà donat pel grau ja sigui d'entrada o de sortida.
