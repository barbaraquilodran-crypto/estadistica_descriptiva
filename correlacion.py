from desviacion_estandar import desviacion_estandar

from covarianza import covarianza
def coeficiente_correlacion(x, y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos variables.
    
    Parámetros:
    -----------
    x, y : list o array
        Dos conjuntos de datos numéricos del mismo tamaño
    
    Retorna:
    --------
    float : Coeficiente de correlación r (-1 ≤ r ≤ 1)
    
    Fórmula:
    --------
    r = Cov(X,Y) / (σ_x * σ_y)
    """
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")
    
    cov_xy = covarianza(x, y)
    std_x = desviacion_estandar(x)
    std_y = desviacion_estandar(y)
    
    if std_x == 0 or std_y == 0:
        return 0
    
    return cov_xy / (std_x * std_y)