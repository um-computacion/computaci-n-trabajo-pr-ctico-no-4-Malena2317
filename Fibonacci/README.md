# Proyecto: Cálculo de la Serie de Fibonacci

Este proyecto implementa la función de la **serie de Fibonacci** en Python, utilizando un enfoque **iterativo**. Además, se incluye un conjunto de **pruebas automatizadas** utilizando `unittest` para validar su correcto funcionamiento bajo distintas condiciones (valores positivos, cero y negativos).

---

## Descripción del problema

La **serie de Fibonacci** es una secuencia matemática donde cada número es la suma de los dos anteriores. La secuencia comienza típicamente con `0` y `1`, y se define de la siguiente manera:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)` para `n > 1`

### Reglas implementadas:
- Si `n` es negativo, la función lanza un `ValueError`.
- Si `n` no es un número entero, también lanza un `ValueError`.
- Para `n = 0`, devuelve 0.
- Para `n = 1`, devuelve 1.
- Para `n > 1`, se calcula iterativamente la suma de los dos términos anteriores.

## Ejecucion de los test
Desde la terminal, ubicándote en la carpeta del proyecto, ejecuta el siguiente comando para correr los tests:
python3 test_fibonacci.py

## Ejemplo de uso 

print(fibonacci(0))   # Resultado: 0
print(fibonacci(1))   # Resultado: 1
print(fibonacci(-1))    # Lanza ValueError
print(fibonacci(3.5))   # Lanza ValueError

## Resultados de los Tests

A continuación se muestra una captura de pantalla de los resultados de los tests ejecutados:

![Resultados de los Tests](https://i.imgur.com/b71EVNB.png)

