def digitosrecursiva(N,digitos=0):
    if N==0:
        return digitos
    else:
        N=N//10
        digitos+=1
        return digitosrecursiva(N,digitos)

print(digitosrecursiva(3000))