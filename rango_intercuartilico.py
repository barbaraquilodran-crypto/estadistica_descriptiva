from estadistica_descriptiva import mediana

def rango_intercuartilico(datos):
    """
    Calcula el rango intercuartílico (RIC = Q3 - Q1)
    reutilizando la función mediana.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos.

    Retorna
    -------
    float
        Rango intercuartílico.
    """
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)

    if n % 2 == 0:
        mitad_inferior = datos_ordenados[:n//2]
        mitad_superior = datos_ordenados[n//2:]
    else:
        mitad_inferior = datos_ordenados[:n//2]
        mitad_superior = datos_ordenados[n//2 + 1:]

    Q1 = mediana(mitad_inferior)
    Q3 = mediana(mitad_superior)

    return Q3 - Q1
