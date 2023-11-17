"""
En este fichero tenemos el algoritmo generado por BackBox AI.
"""

def algoritmo_backbox_raw(arr, low, high, x) -> int:
    """
    Esta función es el código del algoritmo generado por BackBox AI.

    args:
        arr (list): Arreglo de números enteros.
        low (int): Índice bajo.
        high (int): Índice alto.
        x (int): Valor a buscar.

    returns:
        int: Índice del valor buscado.
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return algoritmo_backbox_raw(arr, low, mid - 1, x)
        else:
            return algoritmo_backbox_raw(arr, mid + 1, high, x)
    else:
        return -1



def algoritmo_backbox(x:int, array:list) -> bool:
    """
    Esta función adapta nuestros datos a la función algoritmo_backbox_raw.

    args:
        x (int): Valor a buscar.
        array (list): Arreglo de números enteros.
    
    returns:
        bool: True si el valor está en el arreglo, False si no.
    """
    res = algoritmo_backbox_raw(array, 0, len(array)-1, x)
    return res != -1


if __name__ == '_main__':
    print("Algoritmo generado por BackBox AI")

    # Arreglo de ejemplo
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Función de búsqueda binaria
    result = algoritmo_backbox_raw(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Elemento encontrado en la posición", str(result))
    else:
        print("Elemento no encontrado en el arreglo")