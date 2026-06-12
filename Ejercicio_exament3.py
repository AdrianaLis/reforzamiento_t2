
laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, 0],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 99, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 99, 99],
    [1, 99, 99, 99, 2, 99, 1, 99, 99],
    [-99, 1, 3, 1, 1, 99, 1, 1, 1] 
]

def buscar_camino(f, c, energia, camino):
    if f < 0 or f >= 9 or c < 0 or c >= 9 or laberinto[f][c] == 99:
        return False
    if (f, c) in camino:
        return False
    valor = laberinto[f][c]
    gasto = 0 if valor == -99 or valor == 0 else valor
    if energia - gasto < 0:
        return False
    camino.append((f, c))
    if laberinto[f][c] == -99:
        return True
    movimientos = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    for df, dc in movimientos:
        if buscar_camino(f + df, c + dc, energia - gasto, camino):
            return True
    camino.pop()
    return False
mi_camino = []
if buscar_camino(0, 8, 18, mi_camino):
    print("¡Camino encontrado!:", mi_camino)
else:
    print("No hay camino posible.")