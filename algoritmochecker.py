"""
Este archivo sirve para revisar los algoritmos generados por las IAs y obtener el tiempo de respuesta al desarrollo de cada uno de ellos.

requerimientos:
    - py-cpuinfo
    - psutil
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
    return {
        "array": [i for i in range(1000)],
        "x": 33,
    }
 
def ejecutarAlgoritmos(X: int, array: list):
    """
    Esta función ejecuta los algoritmos de la carpeta algoritmos.
    """
    from algoritmos.algoritmo_chatgpt import algoritmo_chatgpt
    from algoritmos.algoritmo_bard import algoritmo_bard
    from algoritmos.algoritmo_backbox import algoritmo_backbox
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
    pass

if __name__ == '__main__':
    
    # Información del sistema
    print("Información del sistema:")
    sysinfo = systemInfo()
    for key in sysinfo:
        print(f"|   {key.upper()}: {sysinfo[key]}")
        
    # Algoritmos
    resolucion = ejecutarAlgoritmos()
    print("Algoritmos:")
    print(resolucion)