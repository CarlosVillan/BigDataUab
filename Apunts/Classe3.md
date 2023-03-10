# Classe 3

## Tuples

```Python
diccionari = {"clau":"valor"}  
tupla = ("algo","algo")  
  
llista1 = [7,9]  
llista2 = ["josep","cristina"]  
  
llistafinal = []  
for nota, nom in zip(llista1,llista2):  
    conjunt = (nota,nom)  
    llistafinal.append(conjunt)  
  
for t in llistafinal: #Per desempaquetar la tupla  
    nota = t[0]  
    nom = t[1]  
    print(nota,nom)
```


### Ejercicio 1: introducción a Pandas

**Tarea 1:** Unificar los nombres y apellidos de los alumnos en una única cadena de texto
**Tarea* 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida

``` Python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
#Tarea 1: Unificar los nombres y apellidos de los alumnos en una única cadena de texto  
#Tarea 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida  
llista_de_tuples = []  
for nom,cog, nota in zip(alumnes, cognoms, notes):  
    nomcomplet = f"{nom} {cog}"  
    tupla = (nomcomplet,nota)  
    llista_de_tuples.append(tupla)  
print(llista_de_tuples)

#Tarea 3: Sumar un punto a todas la notas, sin que puedan sobrepasar el 10  
  
for persona in llista_de_tuples:  
    nota = persona[1]  
    nova_nota = nota +1  
    if nova_nota > 10:  
        nova_nota = 10  
    nova_persona = (persona[0],nova_nota)  
    print(nova_persona)
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
#Tarea 1: Unificar los nombres y apellidos de los alumnos en una única cadena de texto  
#Tarea 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida  
llista_de_tuples = []  
for nom,cog, nota in zip(alumnes, cognoms, notes):  
    nomcomplet = f"{nom} {cog}"  
    tupla = (nomcomplet,nota)  
    llista_de_tuples.append(tupla)  
#print(llista_de_tuples)  
  
#Tarea 3: Sumar un punto a todas la notas, sin que puedan sobrepasar el 10  
llista_definitiva = []  
for persona in llista_de_tuples:  
    nota = persona[1]  
    nova_nota = nota +1  
    if nova_nota > 10:  
        nova_nota = 10  
    nova_persona = (persona[0],nova_nota)  
  
    if nova_nota < 5:  
        qualy = "Suspendido"  
    elif nova_nota >=5 and nova_nota <=6:  
        qualy = "Aprobado"  
    elif nova_nota > 6 and nova_nota < 7:  
        qualy = "Bien"  
    elif nova_nota >= 7 and nova_nota < 9:  
        qualy = "Notable"  
    elif nova_nota >= 9 and nova_nota < 10:  
        qualy = "Excelente"  
    elif nova_nota == 10:  
        qualy = "Matrícula de honor"  
  
    nova_persona = (persona[0],nova_nota,qualy)  
    llista_definitiva.append(nova_persona)  
print(llista_definitiva)  
  
'''  
Tarea 4: Añadir un tercer elemento a la tupla siguiendo este criterio:  
  
- Si la nota final es inferior a 5, añadir el texto "suspendido".  
- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
- Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".  
- Si la nota es igual o superior a 7, añadir el texto "notable".  
- Si la nota supera el 9, añadir el texto "Excelente".  
- Si la nota equivale a un 10, añadir el texto "matrícula de honor".  
'''
```

## Importar Pandas

Quan es crea un dataframe es declara amb df. 
Pandas read de docs, la forma en que es busca una llibreria. 

```python
Import pandas as pd #estándard

df= pd.DataFrame(llista_definitiva,columns=["nom","nota","quali"])  #S'importa amb el punt dataframe el columns es el nom per cada columna que volem que posi a les tuples que exporti
df.to_excel("dataset.xlsx", index=False) #Arxiu en el que volem que exporti i si index cal o no

df = pd.read_csv("exemple.csv", sep=",") #Cridem a un fitxer cvs que tenim i ens printarà la llista i columnes de l'excel, hi ha mil opcions disponibles dins de cada df amb el que podem delimitar la consulta  
print(df)

```


### Arxius JSON


```python

import pandas as pd  
  
import json  
  
f = open('medidas.json') #Carregar l'arxiu  
data = json.load(f) #transformar en diccionaris  
  
'''¿Cuantas muestras ha capturado el sensor?  
print(len(data))  
  
'''  
  
llista_dades = []  
  
for d in data:  
    temp = d["temperatura"]  
    pres = d["presion"]  
    date = d["fecha"]  
    tupla = temp,pres,date  
    llista_dades.append(tupla)  
  
df = pd.DataFrame(llista_dades, columns=["temp","pres","data"])  
#Ejercicio 2
print(df)  
df.to_csv("temperaturas.csv",index=False, decimal=",")

#Saber cuál ha sido la temperatura máxima, en qué fecha ocurrió  
max = df["temp"].idxmax()  
print(df.iloc[max])
```

