#Ejercicio 1
#Importamos pandas y le asignamos el valor pd.
import pandas as pd

#Cargamos el archivo CSV  mediante pd.read_csv(...).
elenco = pd.read_csv("imdb_elenco.csv")
print(elenco.head(5))

#Realizamos lo mismo que en el anterior apartado pero llamamos a la variable titulos.
titulos = pd.read_csv("imdb_titulos.csv")
print(titulos.head(5))

#Mediante la función titulos.axes contamos el numero de filas o columnas pero al poner [0] nos estamos refieriendo a las filas.
registrostitulos = len(titulos.axes[0])
print("Nº de registros de titulos:",str(registrostitulos))

#Mismo método que el anterior pero en el archivo elenco.
registroselenco = len(elenco.axes[0])
print("Nº de registros de elenco:",str(registroselenco))

#Usando titulos.nsmallest obtiene el valor mínimo y luego le especificamos que queremos los 5 registros más pequeños de la columna "year".
print(titulos.nsmallest(5, "year"))

#Dentro de titulos hacemeos que nos muestren solo aquellos que en la columna "title" sean = a "Dracula".
print(titulos[titulos.title == "Dracula"])

#Calculamos el número mediante len que nos mide el número de filas que tiene la nueva lista.
print(len(titulos[titulos.title == "Dracula"]))

#Para este apartado utilizamos .value_counts() para que haga grupos con los valores que se repiten en la culomna titulos y nos muestre los que más se repiten.
rep = titulos["title"].value_counts()
print(rep)

#Como solo necesitamos los 10 más repetidos pedimos que imprima los 10 primeros con .head(10).
rep.head(10)

#Como nos piden la pélicula llamada "Romeo and Juliet" más antigua primero aislamos todas las llamadas así buscando en titulos.title las que tienen ese nombre.
ryj = titulos[titulos.title == "Romeo and Juliet"]
ryj

#Como necesitamos la más pequeña utilizamos al igual que anteriormente nsmallest en la columna de "year".
ryj.nsmallest(1, ["year"])

#Como necesitamos las peliculas que contengan la palabra "Exorcist" no nos vale con el método del ejercicio anterior por lo que buscamos dentro de title mediante .str.contains("Exorcist) los títulos que contengan esta palabra.
exo = titulos[titulos["title"].str.contains("Exorcist")]
exo

#Los ordenamos de menos a mayor con .sort_values.
exo.sort_values("year")

#Aislamos los registros del año 1950.
pl = titulos[titulos["year"] == 1950]
pl

#Mediante len() calculamos la longitud de la nueva lista.
len(pl)

#Para tener un rango de años primero nos centramos en aquellos > o = a 1950 y luego en la nueva lista nos centramos en los menores o iguales a 1959.
d = titulos[titulos["year"] >= 1950 ]
f = d[titulos["year"] <= 1959]
f

#Buscamos en el apartado "title" de elenco "The Godfather"
e = elenco[elenco.title == "The Godfather"]
e

#Mediante e.iloc [:,4] nos quedamos solo con la columna que buscamos.
c = e.iloc [:,4]
c

#Para ver que valores se repiten utilizamos en la nueva lista c la función value_counts().
papeles = c.value_counts()
papeles

#Buscamos las peliculas que se llamen "Dracula".
drac = elenco[elenco.title == "Dracula"]
drac

#Para ordenarlas por el valor n ordenamos que la lista nueva se ordene de menos a mayor con .nsmallest.
drac.nsmallest(113, ["n"])

#Buscamos el valor "Bruce Wayne" en la columna character.
b = elenco[elenco.character == "Bruce Wayne"]
b

#Medimos la longitud de la lista con len().
len(b)

#Seguimos la misma técnica que en anterior apartado.
r = elenco[elenco.name == "Robert De Niro"]
r
len(r)

#En este caso necesitamos encadenar varias funciones para conseguir la lista con requisitos que nos piden.
s = elenco[elenco.name == "Charlton Heston"]
z = s[elenco.n == 1]
k = z[elenco["year"] >= 1950 ]
k[elenco["year"] <= 1959 ]

#En este apartado nos quedamos con la lista solamente de los años 50´s y luego medimos la longitud en el caso de que sean actores y en el caso de que sean actrices.
w = elenco[elenco["year"] <= 1949]
y = w[elenco["year"] >= 1940]
len(w[elenco.type == "actor"])
len(w[elenco.type == "actress"])