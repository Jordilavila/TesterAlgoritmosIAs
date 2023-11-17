"""
En este fichero tenemos el algoritmo generado por Bard.
"""

def algoritmo_bard_raw(lista, elemento) -> int:
    """
    Esta función es el código del algoritmo generado por Bard.
    
    args:
        lista (list): Arreglo de números enteros.
        elemento (int): Valor a buscar.
    
    returns:
        int: Índice del valor buscado.
    """
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def algoritmo_bard(x:int, array:list) -> bool:
    """
    Esta función adapta nuestros datos a la función algoritmo_bard_raw.

    args:
        x (int): Valor a buscar.
        array (list): Arreglo de números enteros.
    
    returns:
        bool: True si el valor está en el arreglo, False si no.
    """
    res = algoritmo_bard_raw(array, x)
    return res != -1

if __name__ == '__main__':
    print("Algoritmo generado por Bard")
    
    lista = [1, 3, 5, 7, 9]
    elemento = 5
    indice = algoritmo_bard_raw(lista, elemento)
    if indice != -1:
        print("El elemento {} se encuentra en la posición {} de la lista.".format(elemento, indice))
    else:
        print("El elemento {} no se encuentra en la lista.".format(elemento))


