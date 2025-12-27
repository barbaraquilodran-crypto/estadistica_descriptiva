def mediana(vv):
    vals = []
    for e in vv:
        if math.isfinite(e):
            vals.append(e)
    vals.sort()
    #caso impar
    if len(vals)%2!=0:
        k = len(vals)//2
        mediana = vals[k]

    #caso par
    else:
        k = len(vals)//2
        mediana = (vals[k-1]) + vals[k] / 2
        return mediana
            
