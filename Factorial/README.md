# Proyecto: Cálculo del Factorial

Este proyecto consiste en implementar una función en Python para calcular el **factorial** de un número, tanto de manera **iterativa** como **recursiva**. Además, se incluye un conjunto de pruebas automatizadas (TDD) para verificar el comportamiento de la función en diferentes casos.

## Descripción del problema

El **factorial** de un número entero positivo `n` se define como el producto de todos los números enteros desde 1 hasta `n`. Se denota como `n!`, y su fórmula es:

- `n! = n * (n - 1) * (n - 2) * ... * 1`

### Reglas importantes:
- El **factorial de 0** es igual a 1: `0! = 1`
- El **factorial de números negativos** no está definido.
- El **factorial solo está definido para números enteros**. Si se ingresa un número decimal, debe generar un error.

## Ejecucion de los test
Desde la terminal, ubicándote en la carpeta del proyecto, ejecuta el siguiente comando para correr los tests:

python3 test_factorial.py

## Ejemplo de uso 

Factorial de 5:
print(factorial(5))  # Resultado: 120

Factorial de 0:
print(factorial(0))  # Resultado: 1

## Resultados de los Tests

A continuación se muestra una captura de pantalla de los resultados de los tests ejecutados:

![Resultados de los Tests](https://i.imgur.com/TLfiDAO.png)

