def percentil(vals_in, q):
    """
    calcula el percentil. ignora valores NaN
    Parámetros
    ----------
    vals:list
        lista con los valores 
    q: int
        percentil a calcular, entre 0 y 100
    retorna
    -------
    percentil :  float
        el percentil
    """
    #eliminar los valores NaNs
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    #ordenar la ista con los valores in - place
    vals.sort()
    #distancia entre el primer y penultimo elemento
    # a lo largo del eje de los indices 
    dist = len(vals) - 1
    #calcular el "indice efectivo" del percentil
    ieff = dist * q/100
    #aislo la parte fraccional del ieff
    fraction = ieff - int(ieff)
    #aislo la parte entera: corresponde al indice inferior 
    i = int(ieff //1)
    #indice superior
    j = i + 1
    #hacemos una interpolacion entre los valores correspondientes 
    # a los indices encontrados
    percentil  = vals[i] + (vals[j] - vals[i])* fraction
    return percentil
