

def factorial(n): #este esta es la versicion iterativa en ambos casos los test funcionan correctamente
    
    # Comprobar si n es un número negativo
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    # Comprobar si n es un número decimal
    if isinstance(n, float):
        raise ValueError("El factorial solo está definido para números enteros")
    
    # Caso especial: factorial de 0 es 1
    if n == 0:
        return 1
    
    # Implementación iterativa del factorial
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    
    return resultado

# este esta es la versicion recursiva en ambos casos los test funcionan correctamente 

#def factorial(n):
#    # si el numero es menor que cero, tirar error
#    if n < 0:
#        raise ValueError("no se puede con negativos")
#
#    # si es decimal, tirar error tambien
#    if type(n) == float:
#        raise ValueError("tiene que ser un numero entero")
#
#    # si es 0, devolver 1
#    if n == 0:
#        return 1
#
#    # si no, usar recursividad
#    return n * factorial(n - 1)
