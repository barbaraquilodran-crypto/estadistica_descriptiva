def covarianza(x, y, poblacional=True):
    """
    Calcula la covarianza entre dos listas x e y.
    Si poblacional=True usa n en el denominador (covarianza poblacional).
    Si poblacional=False usa n-1 (covarianza muestral).
    """
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    suma = 0
    for i in range(n):
        suma += (x[i] - mean_x) * (y[i] - mean_y)
    
    if poblacional:
        return suma / n
    else:
        return suma / (n - 1)

