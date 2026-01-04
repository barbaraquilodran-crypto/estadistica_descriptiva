def media(datos):
    """
    Calcula la media aritmética de una lista de datos usando solo Python.
    
    Parámetros
    ----------
    datos : list
        Lista de valores numéricos.
    
    Retorna
    -------
    float
        Media aritmética.
    """
    n = len(datos)
    if n == 0:
        return None  # evitar división por cero
    suma = sum(datos)
    return suma / n