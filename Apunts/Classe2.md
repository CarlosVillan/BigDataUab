## Llistes

Exercicis amb llistes

```Python
llista1 = ["adria","carles","julia"]  
  
for nom in llista1:  
    if nom =="joan":  
        print(nom)
    else:  
    print(nom + " no es en joan")

llista1 = ["adria","carles","joan"]  
  
for nom in llista1:  
    if nom =="joan":  
        print(f"{nom} sí es en joan") #Codi més eficient
    else:  
        print(nom + " no es en joan")
```

<>
Validar condicions 
``` Python
numeros = [1,2,3,6,7,8,10]  
  
for n in numeros:  
    if n < 6:  
        print(f"{n} es menor que 6")  
    elif n == 6:  
            print(f"{n} es igual que 6")  
    else:  
        print(f"{n} es major que 6")
```

Print és una funció de Python integrada

``` Python
numeros = [1,2,3,6,7,8,10]  
  
print(len(numeros))  
llargaria = len(numeros) #La diferència es si la usaré després  
print(llargaria)
```

## Exercicis

### Cosas básicas con print()

``` Python
var = "esto es un ejercicio"  
  
print(var)  
  
nota = 2  
  
asignatura = "mates"  
  
print(f"En la asignatura {asignatura} he obtenido un{nota}")

```

### Ejercicios de documentación

Ejercicio A

```Python
var = "esto es un ejercicio"  
  
print(var)  
nota = 2  
asignatura = "mates"  
nota = 10  
frase = f"En la asignatura {asignatura} he obtenido un {nota}"  
print(frase)
```

Ejercicio B
- Per passar de cadena de text a números es fa amb int()
- Per aparellar llistes de dos elements 
- Funció "zip(llista,llista)" per aparellar

```Python
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for nota, nom in zip (notas,alumnos): #Aparellar llistes  
    nota_num = int(nota) #Transforma una cadena en un número  
    nota_final = nota_num + 1   
print (nota_final, nom)

```

## Funcions natives de Python

### Index

Aquesta funció serveix per saber quina posició que ocupa una cosa
``` Python
lista = ["adria", "carla", "joan", "pere"]  
nom = "joan"  
  
if nom in lista:  
    print("si")  
    position = lista.index(nom)  
    print(position)  
else:  
    print("no")
```

### Set

Elimina els valor duplicats d'una llista
``` Python
lista = ["adria", "carla", "joan", "pere","pere","carla"]  
valors_unics = set(lista) #Elimina els valors duplicats  
print(len(valors_unics)) #Per comptar quantes persones reals han vingut
'''print(len(set(lista))) Per reduir-ho a una línia'''
```

### Exercicis 

#### Exercici A

La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?

1.  ¿Cuantas personas han asistido a las jornadas de puertas abiertas?
2.  ¿Cuantas personas han asistido a más de dos sesiones?
3.  ¿Qué porcentaje de los asistentes accede a más de dos sesiones?

```Python
llista = [  
    "david",  
    "dani",  
    "marta",  
    "jaume",  
    "adria",  
    "carla",  
    "joan",  
    "pere",  
    "carla",  
    "pere",  
    "adria",  
    "quico",  
    "pere",  
    "joan",  
    "agustí",  
    "adria",  
    "joan",  
    "adria",  
    "siscu",  
    "carles",  
    "dani",  
    "carla"  
]  
#¿Cuantas personas han asistido a las jornadas de puertas abiertas?  
personas_unicas = set(llista)  
print(f"Han vingut {len((personas_unicas))} alumnes")  
  
#¿Cuantas personas han asistido a más de una sesiones?  
llista_repetits = []  
contador = 0  
for nom in personas_unicas:  
    valor = llista.count(nom)  
    if valor > 1:  
        llista_repetits.append(nom)  
        contador = contador + 1  
print(f"(A) Han vingut  a més de dues sessions {len(llista_repetits)} alumnes")  
print(f"(B) Han vingut  a més de dues sessions {contador} alumnes")  
#¿Qué porcentaje de los asistentes accede a más de una sesiones?  
percentatge = (contador/len(personas_unicas))*100  
print(f"El percentatge d'assistència és del {percentatge}") 
```

### Exercici B

Tienes dos listas, una para notas y otra para el nombre de los alumnos:

1.  Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".
2.  Calcula e imprime la nota promedio del aula con un decimal
3.  Calcula e imprime la nota más alta junto al nombre del alumno.
4.  calcula e imprime la nota más baja junto al nombre del alumno.

```Python
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
  
#Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".  
notes_arreglades = []  
for nota, nom in zip (notes, alumnes):  
    print(f"El alumno/a {nom} ha obtenido un {nota}")  
#Calcula e imprime la nota promedio del aula con un decimal  
    if "." in nota:  
        nota_arreglada = float(nota)  
        notes_arreglades.append(nota_arreglada)  
    elif "," in nota:  
        nota_arreglada = float(nota.replace(",","."))  
        notes_arreglades.append(nota_arreglada)  
    else:  
        nota_arreglada = int(nota)  
        notes_arreglades.append(nota_arreglada)  
  
print(notes_arreglades)  
promig = sum(notes_arreglades)/len(notes_arreglades)  
print(promig)  
print(round(promig,1))  
  
#Calcula e imprime la nota más alta junto al nombre del alumno.  
nota_maxima = max(notes_arreglades)  
posicio = notes_arreglades.index(nota_maxima)  
print(f"La nota máxima és un {nota_maxima}, i l'ha obtingut {alumnes[posicio]}")  
#Calcula e imprime la nota más baja junto al nombre del alumno.  
nota_minima = min(notes_arreglades)  
posicio = notes_arreglades.index(nota_minima)  
print(f"La nota mínima és un {nota_minima}, i l'ha obtingut {alumnes[posicio]}")
```


