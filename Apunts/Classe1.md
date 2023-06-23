
## Llibreries

Les llibreries és la BASE de Python. Depèn de la versió i cada una té unes funcionalitats. Per solucionar això Pycharm genera un entorn virtual. Demana la versió i et crea un entorn de desenvolupament disponible per a cada versió. 

Per descarregar una versió de Python -> Python.org/download

L'arxiu main.py és l'estàndard, el més important d'un projecte de Python.

## Python

Les variables es creen amb un = sense $ ni res

```Python
var = 1
print(var)
```

- Los bucles se cierran con dos puntos :
- Control + C per aturar el procés en la consola de Python 
- Control + L per netejar el terminal
- Funció "str()" és una funció que converteix un valor específic en string

Es poden sobreescriure les variables, són mutables. Manarà l'última.
```Python
var= 10 
var = var + 1
print(var) #El resultat serà 11
```

- "#" Per comentar
- Tres cometes per cometar més d'una fila

 ``` Python
var= [1,2,3,4,5] #Això és una llista
'''var = 201
varl = 230 esto es un comentario de bloque'''
for num in var:
	print (num)
```

f 'XXX' davant de tot. La variable va en claudàtor {} 
```Python
noms = ['carlos','pau','alex','pol']  
for nom in noms:  
    print(f'En {nom} no ha vingut') #Recorre tota la llista sense fer un for
```


 ## Obsidian
Coses bàsiques del programa:
#etiqueta #prova
# Títol 1 (# )
## Títol 2 (## )
### Títol 3 (### )
I així seguidament.
```
Això és un text de codi i s'ha d'obrir amb (```)
```

## Remember de Python
### Cadena de text
Hi ha problemes amb les cometes, no confondre-les.
--> Utilitzar simples/dobles
Els dos exemples són cadenes de text.
``` "cadena de text" 'cadena de text' ```

### Print
--> Mostrar a pantalla el que sigui
--> Cal separar amb comes els diferents tipus de coses:
```"L'usuari", usuari, "té", likes, "likes."```

### Números
--> Integers: sense punt: 1
--> Float: amb punt: 1.2
--> Per passar de string a integer: int(numero_string)
```Python
for n in notas:  
    nota_numerica = int(nota)
```

### Variables
--> Text directament escrit amb un igual al final: nom_variable = 1
--> Les variables es poden sobreescriure, la que mana és la última per ordre de lectura del text.

### Funcions
#### str
--> Uneix diferents tipus de dades en un string:

### Comentaris
--> Per fer comentaris utilitzar el hashtag (#)
--> Les tres cometes creen un paragraf de comentari
```
"""Això és un comentari""" 
# Això també és un comentari
``` 

