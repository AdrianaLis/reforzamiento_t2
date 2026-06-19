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
    if lab[f][c] == -2: costo = 2
    
    return (vidas - costo) > 0

def sollab(lab, res, f, c, vidas):
    valor = lab[f][c]
    costo = 1 if valor == -1 else (2 if valor == -2 else 0)
    nuevavida = vidas - costo
    res[f][c] = 1
    imprime(res)
    

    if f == 0 and c == 0:
        return True
    for df, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
        nf, nc = f + df, c + dc
        if es_valido(lab, res, nf, nc, nuevavida):
            if sollab(lab, res, nf, nc, nuevavida):
                return True
            
    res[f][c] = 0
    return False
laberinto = [
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

print("Laberinto Original:")
imprime(laberinto)

# Inicia en esquina inferior izquierda (8,0) con 3 vidas
if sollab(laberinto, res, 8, 0, 3):
    print("¡El ratón ha logrado salirrr!")
else:
    print("El ratón no pudo encontrar una salida con 3 vidas.")