## Proyecto: Aplanar Estructuras de Datos Anidadas

Este proyecto consiste en el desarrollo de una función recursiva en Python que permite **aplanar listas** que contienen otras listas, tuplas o diccionarios en su interior. Forma parte de un trabajo práctico orientado al aprendizaje de **recursividad** y **pruebas automatizadas (TDD)**.
 
## Descripción del problema

Cuando se trabaja con estructuras de datos en Python, es común encontrarse con listas que contienen otras listas u objetos anidados. Este tipo de estructuras dificultan el procesamiento de los datos si se necesita trabajar con una lista “plana” o lineal. Por ejemplo:

[1, [2, 3], (4, [5, 6]), {"a": 7, "b": [8, 9]}]

El objetivo es construir una funcion que transforme esa lista en 

[1, 2, 3, 4, 5, 6, "a", 7, "b", 8, 9]

## Ejecucion de los test

Desde la termina  ubicandore en la carpeta del poryecto ejecuta:

python3 test_flatten.py

## Ejemplo de uso 

-Lista simple

aplanar_lista([1, 2, 3])
# Resultado: [1, 2, 3]

-Lista con tuplas y diccionarios 

aplanar_lista([1, (2, 3), {'a': 4, 'b': [5, 6]}, [7, [8]]])
# Resultado: [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]

## Resultados de los Tests

A continuación se muestra una captura de pantalla de los resultados de los tests ejecutados:

![Resultados de los Tests](https://imgur.com/a/KdcEcQp)



