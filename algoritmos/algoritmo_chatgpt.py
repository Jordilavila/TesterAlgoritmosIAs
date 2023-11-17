"""
En este fichero tenemos el algoritmo generado por ChatGPT.
"""

def algoritmo_chatgpt_raw(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # Verificar si el objetivo está en la mitad
        if arr[medio] == objetivo:
            return medio
        # Si el objetivo es menor, descartar la mitad derecha
        elif arr[medio] > objetivo:
            derecha = medio - 1
        # Si el objetivo es mayor, descartar la mitad izquierda
        else:
            izquierda = medio + 1

    # Si no se encuentra el objetivo
    return -1

def algoritmo_chatgpt(x: int, array: list) -> bool:
    """
    Esta función adapta nuestros datos a la función algoritmo_chatgpt_raw.

    args:
        x (int): Valor a buscar.
        array (list): Arreglo de números enteros.
    
    returns:
        bool: True si el valor está en el arreglo, False si no.
    """
    res = algoritmo_chatgpt_raw(array, x)
    return res != -1

if __name__ == '__main__':
    print("Algoritmo generado por ChatGPT")

    # Ejemplo de uso
    lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    objetivo = 7

    resultado = algoritmo_chatgpt_raw(lista_ordenada, objetivo)

    if resultado != -1:
        print(f"El elemento {objetivo} está en la posición {resultado}.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista.")
    
    