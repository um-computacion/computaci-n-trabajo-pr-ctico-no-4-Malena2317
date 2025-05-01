
def aplanar_lista(lista):
    # Creamos una lista vacía donde vamos a guardar los resultados
    resultado = []

    # Recorremos cada elemento de la lista
    for item in lista:
        # Si el item es una lista
        if type(item) == list:
            # Llamamos a la función de nuevo para aplanar la sublista
            resultado += aplanar_lista(item)  # Usamos "+" para agregar lo aplanado a la lista
        # Si el item es una tupla
        elif type(item) == tuple:
            # Llamamos a la función de nuevo para aplanar la tupla
            resultado += aplanar_lista(item)
        # Si el item es un diccionario
        elif type(item) == dict:
            # Agregamos las claves y los valores
            for clave, valor in item.items():
                resultado.append(clave)
                resultado.append(valor)
        else:
            # Si el item no es una lista, tupla o diccionario, lo agregamos directamente
            resultado.append(item)

    # Al final devolvemos la lista aplanada
    return resultado
