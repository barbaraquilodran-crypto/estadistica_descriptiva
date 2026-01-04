def mad(vals,in):
    
     """
    calcula el MAD d una distribucion. ignora valores NaN
    Parámetros
    ----------
    vals:list
        lista con los valores 
    retorna
    -------
    mad :float
    la desviacion absoluta de los datos
    """
    #eliminar los valores NaNs
    vals =[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
#CALCULAR MEDIANA 
    med = mediana(vals)#COLOCAR EL NOMBRE DE COMO YA TENGO GUARDADA LA MEDIANA
    desviaciones_absolutas = []
    for v in vals:
    desviaciones_abs.append(abs(v -  med))
        mad = mediana(desviaciones_abs)
    return mad
