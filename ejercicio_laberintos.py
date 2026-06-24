def qcamFRB(f, c, n):
    global contador
    contador += 1
    
    if f == n - 1 and c == n - 1:
        return 1
    elif f == n - 1:
        return qcamFRB(f, c + 1, n)
    elif c == n - 1:
        return qcamFRB(f + 1, c, n)
    else:
        return qcamFRB(f, c + 1, n) + qcamFRB(f + 1, c, n)


def qcamPDR(n):
   
    matriz = [[-1 for _ in range(n)] for _ in range(n)]
    return qcamPDRU(0, 0, n, matriz)

def qcamPDRU(f, c, n, matriz):
    global contador
    contador += 1
    

    if matriz[f][c] != -1:
        return matriz[f][c]
    
    if f == n - 1 and c == n - 1:
        resultado = 1
    elif f == n - 1:
        resultado = qcamPDRU(f, c + 1, n, matriz)
    elif c == n - 1:
        resultado = qcamPDRU(f + 1, c, n, matriz)
    else:
        resultado = qcamPDRU(f, c + 1, n, matriz) + qcamPDRU(f + 1, c, n, matriz)
    
    matriz[f][c] = resultado
    return resultado


n = 6

contador = 0
print(f"Resultado PD: {qcamPDR(n)} | Contador PD: {contador}")

contador = 0
print(f"Resultado FB: {qcamFRB(0, 0, n)} | Contador FB: {contador}")