def cuartiles(datos):
    """
    Calcula Q1 y Q3 de una lista de datos usando solo Python.
    
    Parámetros
    ----------
    datos : list
        Lista de valores numéricos.
    
    Retorna
    -------
    q1 : float
        Primer cuartil (percentil 25).
    q3 : float
        Tercer cuartil (percentil 75).
    """
    # Ordenar los datos
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    # Mediana general
    def mediana(lista):
        m = len(lista)
        if m % 2 == 0:
            return (lista[m//2 - 1] + lista[m//2]) / 2
        else:
            return lista[m//2]
    
    # Dividir en mitades
    if n % 2 == 0:
        lower_half = datos_ordenados[:n//2]
        upper_half = datos_ordenados[n//2:]
    else:
        lower_half = datos_ordenados[:n//2]   # excluye la mediana
        upper_half = datos_ordenados[n//2+1:] # excluye la mediana
    
    q1 = mediana(lower_half)
    q3 = mediana(upper_half)
    
    return q1, q3