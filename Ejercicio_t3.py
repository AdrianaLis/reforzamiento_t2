def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def es_valido(lab, res, f, c, vidas):
    if f < 0 or f >= 9 or c < 0 or c >= 9:
        return False
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    costo = 0
    if lab[f][c] == -1: costo = 1
    elif lab[f][c] == -2: costo = 2
    return (vidas - costo) > 0

def sollab(lab, res, f, c, vidas):
    if not es_valido(lab, res, f, c, vidas):
        return False
    valor = lab[f][c]
    costo = 1 if valor == -1 else (2 if valor == -2 else 0)
    nuevas_vidas = vidas - costo
    res[f][c] = 1
    imprime(res)
    if f == 0 and c == 0:
        return True
    if sollab(lab, res, f + 1, c, nuevas_vidas): return True
    if sollab(lab, res, f, c + 1, nuevas_vidas): return True
    if sollab(lab, res, f - 1, c, nuevas_vidas): return True
    if sollab(lab, res, f, c - 1, nuevas_vidas): return True
    res[f][c] = 0
    return False

lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, -1, 1, 1, 1, 0, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

if sollab(lab, res, 8, 0, 3):
    print("¡El ratón ha logrado salir!")
else:
    print("No se encontró salida.")