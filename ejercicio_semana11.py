def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, res, f, c):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    return True

def sollab(lab, res, f, c):
    if valido(lab, res, f, c):
        res[f][c] = 1
        imprime(res)
        
        # Condición de éxito al pisar la meta
        if f == 2 and c == 0:
            return True
            
        # Movimientos condicionales (If / Elif)
        if sollab(lab, res, f, c + 1):      # Derecha
            return True
        elif sollab(lab, res, f + 1, c):    # Abajo
            return True
        elif sollab(lab, res, f - 1, c):    # Arriba
            return True
        elif sollab(lab, res, f, c - 1):    # Izquierda
            return True
            
        # Backtracking puro (borra si el camino falló)
        res[f][c] = 0
        return False
    else:
        return False

# --- TU MATRIZ DE EXCEL ---
laberinto = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1]
]

resultado = [[0] * len(laberinto[0]) for _ in range(len(laberinto))]

# Ejecución
if sollab(laberinto, resultado, 0, 0):
    print(" resuelto con éxito en la posición (2,0)")
else:
    print("No se encontró una solución válida.")