def rango(vals_in):
    
#    """
    calcula el rango de una lista de numeros.
    detecta y elimina Nan
    parametros
    -----------------
    vals in:lista
    lista con los numeros

    retorna
    -----------------
    rango : float
    el rango de numeros (excluyendo nans)
    #eliminar valores Nan
    
    vals=[]
    for v in vals in:
        if math.isfinite(v):#quitee nans
            vals.append(v)
    #determinar min ymax
    minimo = vals[0]
    maximo = vals[0]
    for v in vals:
        if v < minimo:
            minimo = v
        if v > maximo:
            maximo = v
    return maximo - minimo
