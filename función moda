def moda(vals):
    
    categorias = []
    for v in vals:
        if v not in categorias:
            categorias.append(v)
    frecuencias = []
    for c in categorias:
        contador = 0
        for v in vals:
            if v == c:
                contador += 1
        frecuencias.append(contador)
    max_frec = max(frecuencias)
    modas = []
    for i in range(len(categorias)):
        if frecuencias[i] == max_frec:
            modas.append(categorias[i])
    if len(modas) == 1:
        return modas[0]
    return modas
