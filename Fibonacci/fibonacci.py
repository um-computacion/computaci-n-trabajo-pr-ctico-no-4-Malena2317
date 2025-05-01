

def fibonacci(n): # este codigo es la version iterativa de la implentacion de la funcion fibonacci 

    # Ver si n es negativo
    if n < 0:
        raise ValueError("no se puede con numeros negativos")

    # Ver si n no es un entero
    if type(n) != int:
        raise ValueError("solo se puede con enteros")

    # Casos especiales
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Calcular con iteración
    a = 0
    b = 1
    contador = 2
    while contador <= n:
        c = a + b
        a = b
        b = c
        contador = contador + 1

    return b


# def fibonacci(n): #este codigo es la version recursiva de la implemtacion de la ufncion fibonacci 

#     # Si el número es negativo, tirar un error
#     if n < 0:
#         raise ValueError("no se puede con numeros negativos")
# 
#     # Si no es un entero, tirar otro error
#     if type(n) != int:
#         raise ValueError("solo se puede con enteros")
# 
#     # Si es 0, devolver 0
#     if n == 0:
#         return 0
# 
#     # Si es 1, devolver 1
#     if n == 1:
#         return 1
# 
#     # Si no, llamar a la función otra vez con n-1 y n-2
#     return fibonacci(n - 1) + fibonacci(n - 2)
