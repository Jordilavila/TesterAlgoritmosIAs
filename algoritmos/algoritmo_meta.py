"""
En este fichero tenemos el algoritmo generado por Meta Llama 2.
"""

def algoritmo_meta_raw(arr, x) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def algoritmo_meta(x:int, array:list) -> bool:
    """
    Esta función adapta nuestros datos a la función algoritmo_meta_raw.

    args:
        x (int): Valor a buscar.
        array (list): Arreglo de números enteros.
    
    returns:
        bool: True si el valor está en el arreglo, False si no.
    """
    res = algoritmo_meta_raw(array, x)
    return res != -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 10
    result = algoritmo_meta_raw(arr, x)
    print(result)