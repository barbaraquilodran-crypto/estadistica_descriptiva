"""
Función para calcular la Desviación Absoluta de la Mediana (MAD)
"""

from mediana import mediana

def mad(datos):
    """
    Calcula la Desviación Absoluta de la Mediana (MAD).
    
    Parámetros:
    -----------
    datos : list o array
        Conjunto de datos numéricos
    
    Retorna:
    --------
    float : MAD de los datos
    
    Fórmula:
    --------
    MAD = mediana(|x_i - mediana(x)|)
    """
    # Calcular la mediana de los datos
    m = mediana(datos)
    
    # Calcular las desviaciones absolutas respecto a la mediana
    desviaciones_absolutas = [abs(x - m) for x in datos]
    
    # Retornar la mediana de las desviaciones absolutas
    return mediana(desviaciones_absolutas)
