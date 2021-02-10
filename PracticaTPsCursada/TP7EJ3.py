def SumaNaturales(N,M=0,suma=0):
    if N==M:
        return suma
    else:
        M+=1
        suma=suma+M
        return SumaNaturales(N,M,suma)
    
print(SumaNaturales(5))