def desviacion_estandar(datos):

    # 1. media
    media = sum(datos) / len(datos)
    
    # 2. la suma de los cuadrados de las diferencias
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    
    # 3. Varianza muestral 
    varianza = suma_cuadrados / (len(datos) - 1)
    
    # 4. Raíz cuadrada de la varianza
    return math.sqrt(varianza)
