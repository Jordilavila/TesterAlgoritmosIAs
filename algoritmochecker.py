"""
Este archivo sirve para revisar los algoritmos generados por las IAs y obtener el tiempo de respuesta al desarrollo de cada uno de ellos.

Requisitos:
    - py-cpuinfo
    - psutil
    - numpy

    Se instalan con el comando:  
        `pip install py-cpuinfo psutil numpy`

    O bien, con el comando:
        `pip install -r requirements.txt`
"""

FOLDER_ALGORITMOS = "algoritmos"

def parseOSname(osname: str) -> str:
    """
    Esta función se encarga de parsear el nombre del sistema operativo.
    
    args:
        osname: nombre del sistema operativo
    return: str
    """
    SOs = {
        "Linux": "Linux",
        "Darwin": "MacOS",
        "Windows": "Windows"
    }
    return SOs[osname]

def systemInfo() -> dict:
    """
    Esta función obtiene la información del sistema y la devuelve en un diccionario.
    
    return: dict
    """
    import platform, psutil, cpuinfo
    return {
        "so": " " + parseOSname(platform.system()),
        "cpu": cpuinfo.get_cpu_info()['brand_raw'],
        "arq": platform.machine(),
        "ram": str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    }
    
def variablesStock() -> dict:
    """
    Esta función genera las variables de stock y las devuelve en un diccionario.
    
    return: dict
    """
    import numpy as np
    array = np.arange(500000000)
    return {
        "array": array.tolist(),
        "x": 33,
    }
 
def ejecutarAlgoritmos(X: int, array: list):
    """
    Esta función ejecuta los algoritmos de la carpeta algoritmos.
    """
    import time
    from algoritmos.algoritmo_chatgpt import algoritmo_chatgpt
    from algoritmos.algoritmo_bard import algoritmo_bard
    from algoritmos.algoritmo_blackbox import algoritmo_backbox
    from algoritmos.algoritmo_meta import algoritmo_meta
    algoritmos = {
        "valor_buscado": X,
        "algoritmos": [
            {
                "nombre": "ChatGPT",
                "tiempo": 0,
            },
            {
                "nombre": "Bard",
                "tiempo": 0,
            },
            {
                "nombre": "BackBox AI",
                "tiempo": 0,
            },
            {
                "nombre": "Meta Llama 2",
                "tiempo": 0,
            }
        ]
    }

    # ChatGPT
    start = time.time()
    algoritmo_chatgpt()
    end = time.time()
    algoritmos["algoritmos"][0]["tiempo"] = round((end - start) * 1000, 3)

    # Bard
    start = time.time()
    algoritmo_bard(X, array)
    end = time.time()
    algoritmos["algoritmos"][1]["tiempo"] = round((end - start) * 1000, 3)

    # BackBox AI
    start = time.time()
    algoritmo_backbox(X, array)
    end = time.time()
    algoritmos["algoritmos"][2]["tiempo"] = round((end - start) * 1000, 3)

    # Meta Llama 2
    start = time.time()
    algoritmo_meta()
    end = time.time()
    algoritmos["algoritmos"][3]["tiempo"] = round((end - start) * 1000, 3)

    return algoritmos

if __name__ == '__main__':
    
    # Información del sistema
    print("Información del sistema:")
    sysinfo = systemInfo()
    for key in sysinfo:
        print(f"|   {key.upper()}: {sysinfo[key]}")
        
    # Algoritmos
    print("\nVariables de stock:")
    variables = variablesStock()
    print("Dato a buscar:", variables["x"])
    print("Elementos del array:", len(variables["array"]))

    # Resultados (tiempos de ejecución en milisegundos)
    resolucion = ejecutarAlgoritmos(variables["x"], variables["array"])
    print("Resultados (tiempos de ejecución en milisegundos):")
    print(resolucion)

    # Impresión de resultados
    print("\nResultados:")
    for algoritmo in resolucion["algoritmos"]:
        print(f"|   {algoritmo['nombre']}: {algoritmo['tiempo']} ms")
